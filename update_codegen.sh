docker run --rm -v `pwd`:/base swaggerapi/swagger-codegen-cli-v3 generate -l python-flask -o /base -i /base/swagger_server/swagger/swagger.yaml
