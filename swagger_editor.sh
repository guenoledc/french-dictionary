
PROG=`which swagger-editor-live`

if [ "$?" != "0" ]
then
  echo "install swagger editor live with 'npm install swagger-editor-live -g'"
  exit 1
fi

$PROG swagger_server/swagger/swagger.yaml --port=8081 &