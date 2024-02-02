from fastapi import FastAPI
from ariadne.asgi import GraphQL
from src.schema.types import schema
from ariadne.validation import cost_validator
import uvicorn

app = FastAPI()
print("running app.py")
# type_defs = load_schema_from_path("graphql/schema.graphql")
# resolvers = [query, mutation, subscription]
# schema = make_executable_schema(type_defs, resolvers, snake_case_fallback_resolvers)

graphQL = GraphQL(schema, debug=False, validation_rules=[cost_validator(maximum_cost=5)])


app.mount("/", graphQL)

# app = GraphQL(schema, debug=True)






# from ariadne import QueryType, make_executable_schema, load_schema_from_path
# from ariadne.asgi import GraphQL

# type_defs = load_schema_from_path("schema.graphql")

# query = QueryType()


# @query.field("hello")
# def resolve_hello(*_):
#     return "Hello world!"


# schema = make_executable_schema(type_defs, query)
# app = GraphQL(schema, debug=True)
if __name__=='__main__':
    uvicorn.run(host="0.0.0.0", port=8008, app=app)
