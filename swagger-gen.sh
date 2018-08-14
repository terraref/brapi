# Regenerate based on the Swagger spec

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
    -i https://app.swaggerhub.com/apiproxy/schema/file/PlantBreedingAPI/BrAPI/1.3/swagger.json \
    -l python-flask \
    -c /local/config.json \
    -t /local/templates/flaskConnexion \
	-o /local 
