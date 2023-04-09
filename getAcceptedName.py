#This is a web server wrapping the WFO GraphQL API with a simple rest API for getting accepted plant names
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
  return "This is an api! Try /acceptedname"

@app.route("/acceptedname")
def acceptedname():
  name = request.args.get('name')
  if name is None:
    return jsonify({})
  
  query = f'''query {{
      taxonNameMatch(inputString: "{name}") {{
      inputString
      match {{
        id
        identifiersOther {{
          kind
          value
        }}
        fullNameStringPlain
        currentPreferredUsage {{
          hasName {{
            fullNameStringPlain
            nomenclaturalStatus
          }}
        }}
        nomenclaturalStatus
      }}
    }}
  }}
  '''
  
  transport = RequestsHTTPTransport(url='https://list.worldfloraonline.org/gql.php')
  client = Client(transport=transport, fetch_schema_from_transport=True)
  query = gql(query)

  result = client.execute(query)
  return jsonify(result)


if __name__ == '__main__':
  app.run(port=5000, debug=False)