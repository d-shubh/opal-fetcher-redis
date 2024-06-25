#!/bin/sh
# Pre-populating redis data for testing
redis-server --daemonize yes --appendonly yes --requirepass $REDIS_PASSWORD
echo "Started Redis server..."

# Users
redis-cli -a $REDIS_PASSWORD HSET user:alice roles '["admin"]' location '{"country": "US", "ip": "8.8.8.8"}'
redis-cli -a $REDIS_PASSWORD HSET user:bob roles '["employee", "billing"]' location '{"country": "US", "ip": "8.8.8.8"}'
redis-cli -a $REDIS_PASSWORD HSET user:sunil roles '["guest"]' location '{"country": "US", "ip": "8.8.8.8"}'
redis-cli -a $REDIS_PASSWORD HSET user:eve roles '["customer"]' location '{"country": "US", "ip": "8.8.8.8"}'

# Role Permissions
redis-cli -a $REDIS_PASSWORD HSET role:customer permissions '[{"action": "read", "type": "dog"}, {"action": "read", "type": "cat"}, {"action": "adopt", "type": "dog"}, {"action": "adopt", "type": "cat"}]'
redis-cli -a $REDIS_PASSWORD HSET role:employee permissions '[{"action": "read", "type": "dog"}, {"action": "read", "type": "cat"}, {"action": "update", "type": "dog"}, {"action": "update", "type": "cat"}]'
redis-cli -a $REDIS_PASSWORD HSET role:billing permissions '[{"action": "read", "type": "finance"}, {"action": "update", "type": "finance"}]'
redis-cli -a $REDIS_PASSWORD HSET role:guest permissions '[{"action": "read", "type": "cat"}, {"action": "read", "type": "finance"}]'

tail -f /dev/null
