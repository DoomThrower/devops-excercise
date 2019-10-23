## Tasks from TODO:
- [ ] **src/backend**: Locate and fix security breach - 1h30m
- [ ] **src/backend**: Improve number of requests per second **/cpu** and **/local_program** endpoints 
      (architecture-wise approach - separate monolith, provide additional containers) - 1h30m
- [ ] **src/backend**: Provide a solution for the cache with multi-service awareness - 1h30m
- [x] **Dockerfile**: Fix issue with needless steps in docker image on every code change - 15m
- [x] **docker-compose.yml**: Change database to something more appropriate for key-value storage 
      (noSQL: mongoDB/Redis; take high availability and resilience into consideration) - 2h30m

## Tasks from README (may somewhat overlap with tasks above):
- Improve the architecture to increase the performance, reliability and the availability of the system:
  - [x] Separate monolith (2 services: **db access** and **cpu/local_program**) -1h30m (accounted earlier)
  - [x] Replace db service with something more scalable/resilient - 2h30m (accounted earlier)
- Add monitoring and measurement to the project (prometheus/grafana metrics)
  - [ ] Add prometheus metrics to code - 45m
  - [ ] Add prometheus container - 15m
  - [ ] Add grafana container - 15m
  - [ ] Provide basic grafana dashboards - 45m
- Centralize all logs (ELK stack probably)
  - [ ] Solve how to aggregate docker logs - 1h
  - [ ] Add ELK stack containers (unless something better/easier will appear during research) - 2h

# My task suggestions (based on code provided):
- [x] **src/backend**: Fix the cpu() method in (curl returns 500 error rather than value) - 5m
- [x] **src/backend**: Verify that the cache solution implemented is working at all (**cache[name] = None**
      does not seem like it stores the age value and my guess is it should) - 5m
      
      My suspicion was wrong - this line is responsible for clearing cache prior to inserting new data.
      
- [ ] **src/backend**: Refactor database access code (hardcoded credentials/endpoint, connection probably should 
      not be initiated on every request) - 45m
- [ ] Prepare load-testing commands (e.g. curl), verifying consistency of the application - 45m
- [ ] Understand the nature of **cpu/local_program** endpoints (it could be possible to store a set of pre-computated 
      values for them using some sort of producer/consumer approach in order to increase requests-per-second) - 0m
- [ ] Add Edge Load Balancer (I want to separate monolith, but still the endpoints should remain intact, preferably 
      regardless of amount of service containers) - 1h
- [ ] Verify that there was an issue in the caching mechanism of **db_service** in the initial code (see: last paragrph
      of section 3.)
      
# 1. Approach:
Based on these tasks, I estimate that fulfilling them would take me about 15 hours - that is, obviously, assuming no 
unforeseen complications occur. As such, I believe I will be done by **october 24th, 8PM GMT+2** (1st lvl deadline).

Still, as a precaution, I would like to extend this deadline by 24 hours (2nd lvl deadline: **october 25th, 8PM GMT+2**).

# 2. Seprating monolith:
Since we would like to increase amount of requests-per-second to the **/cpu** and **/local_program** endpoints,
I separated monolith we had into 2 services:
- cpu_service - providing **/cpu** and **/local_program** endpoints - this will be scaled later (architectural approach)
- db_service - providing **/age** endpoint - this does not need to be scaled

Note that right now, **cpu_service** listens on port 8081 and **db_service** listens on port 8080 (see: docker-compose).
I will resolve this later, when I will add Edge Load Balancer.

# 3. Replacing database
As noted in the **docker-compose.yml**, PostgreSQL is not the best approach when it comes to key-value storage. As such,
I decided that a noSQL approach will be better (mongoDB was selected).

As I've had some good experience with [Bitnami](https://bitnami.com/) solutions, I've looked into what they have to
offer when it comes to mongoDB. Lo and behold: https://hub.docker.com/r/bitnami/mongodb/ offers neat docker-compose for
scalable mongoDB stack.

One of the more interesting features is the pre-init - both database, as well as user credentials can be set using only
environment variables, making init query scripts obsolete (see: `MONGODB_USERNAME`, `MONGODB_PASSWORD` and 
`MONGODB_DATABASE` environment variables in the **docker-compose.yml** file).

Now, scaling of mongodb cluster is as simple as: 

```docker-compose up --detach --scale mongodb-primary=1 --scale mongodb-secondary=3 --scale mongodb-arbiter=1```

This will scale secondary mongodb containers to 3.

Also, I did notice some network issues when restarting the application via `docker-compose up/down`. Luckily, 
[Bitnami](https://bitnami.com/) is documented well enough to address this potential issue with ephemeral IPs (see: 
`MONGODB_ADVERTISED_HOSTNAME`, both in **docker-compose.yml** file and at https://hub.docker.com/r/bitnami/mongodb/).

It is important to note, that although my approach provides scalable and resilient noSQL database, its replication is
not configured properly (thus the `Replication has not yet been configured` message in mongoDB logs). Due to time
constraints, I consider this aspect as an out-of-scope for this excercise.

Last issue I noticed was the strange behaviour of application in a specific scenario: When trying to GET age list of
a specific user **after** PUTting his age, caching mechanism seemed to be not working properly (returned `null` rather
than the list). I located and resolved the issue in the **db_service/src/backend.py** - `put_age()` method sets `cache`
value to `None`, but `get_age()` method was checking only if the key in `cache` exists and **not** the value. Will need
to verify that scenario on the initial code (task added).