## Tasks from TODO:
- [ ] **src/backend**: Locate and fix security breach - 1h30m
- [ ] **src/backend**: Improve number of requests per second **/cpu** and **/local_program** endpoints 
      (architecture-wise approach - separate monolith, provide additional containers) - 1h30m
- [ ] **src/backend**: Provide a solution for the cache with multi-service awareness - 1h30m
- [ ] **Dockerfile**: Fix issue with needless steps in docker image on every code change - 15m
- [ ] **docker-compose.yml**: Change database to something more appropriate for key-value storage 
      (noSQL: mongoDB/Redis; take high availability and resilience into consideration) - 2h30m

## Tasks from README (may somewhat overlap with tasks above):
- Improve the architecture to increase the performance, reliability and the availability of the system:
  - [ ] Separate monolith (2 services: **db access** and **cpu/local_program**) -1h30m (accounted earlier)
  - [ ] Replace db service with something more scalable/resilient - 2h30m (accounted earlier)
- Add monitoring and measurement to the project (prometheus/grafana metrics)
  - [ ] Add prometheus metrics to code - 45m
  - [ ] Add prometheus container - 15m
  - [ ] Add grafana container - 15m
  - [ ] Provide basic grafana dashboards - 45m
- Centralize all logs (ELK stack probably)
  - [ ] Solve how to aggregate docker logs - 1h
  - [ ] Add ELK stack containers (unless something better/easier will appear during research) - 2h

# My task suggestions (based on code provided):
- [ ] **src/backend**: Fix the cpu() method in (curl returns 500 error rather than value) - 5m
- [ ] **src/backend**: Verify that the cache solution implemented is working at all (**cache[name] = None**
      does not seem like it stores the age value and my guess is it should) - 5m
- [ ] **src/backend**: Refactor database access code (hardcoded credentials/endpoint, connection probably should 
      not be initiated on every request) - 45m
- [ ] Prepare load-testing commands (e.g. curl), verifying consistency of the application - 45m
- [ ] Understand the nature of **cpu/local_program** endpoints (it could be possible to store a set of pre-computated 
      values for them using some sort of producer/consumer approach in order to increase requests-per-second) - 0m
- [ ] Add Edge Load Balancer (I want to separate monolith, but still the endpoints should remain intact, preferably 
      regardless of amount of service containers) - 1h
      
# 1. Approach:
Based on these tasks, I estimate that fulfilling them would take me about 15 hours - that is, obviously, assuming no 
unforeseen complications occur. As such, I believe I will be done by **october 24th, 8PM GMT+2** (1st lvl deadline).

Still, as a precaution, I would like to extend this deadline by 24 hours (2nd lvl deadline: **october 25th, 8PM GMT+2**).