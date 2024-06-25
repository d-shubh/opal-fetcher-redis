<p  align="center">
 <img src="https://github.com/permitio/opal/assets/4082578/4e21f85f-30ab-43e2-92de-b82f78888c71" height=170 alt="opal" border="0" />
</p>
<h2 align="center">
OPAL Fetcher for Redis
</h2>

[Check out OPAL main repo here.](https://github.com/permitio/opal)

### What's in this repo?
An OPAL to bring authorization state from [Redis](https://redis.io).

This fetcher is both:
- **A fully functional fetch-provider for Redis:** can be used by OPAL to fetch data from Redis.
- **Serving as an example** how to write custom fetch providers for OPAL.

### How to try this custom fetcher in one command? (Example docker-compose configuration)

You can test this fetcher with the example docker compose file in this repository root. Clone this repo, `cd` into the cloned repo, and then run:
```
docker compose up
```
this docker compose configuration already correctly configures OPAL to load the Redis Fetch Provider, and correctly configures `OPAL_DATA_CONFIG_SOURCES` to include an entry that uses this fetcher.


### 📖 About OPAL (Open Policy Administration Layer)
[OPAL](https://github.com/permitio/opal) is an administration layer for Open Policy Agent (OPA), detecting changes to both policy and policy data in realtime and pushing live updates to your agents.

OPAL brings open-policy up to the speed needed by live applications. As your application state changes (whether it's via your APIs, DBs, git, S3 or 3rd-party SaaS services), OPAL will make sure your services are always in sync with the authorization data and policy they need (and only those they need).

Check out OPAL's main site at [OPAL.ac](https://opal.ac).

<img src="https://i.ibb.co/CvmX8rR/simplified-diagram-highlight.png" alt="simplified" border="0">
