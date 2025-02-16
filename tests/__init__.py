"""
Primary initialization, here we fill
necessary variables for the test environment
"""

from os import environ as env

env["POSTGRES_HOST"] = "localhost"
env["POSTGRES_PORT"] = "5433"
env["POSTGRES_USER"] = "admin"
env["POSTGRES_PASSWORD"] = "password"
env["POSTGRES_DB"] = "postgres"
