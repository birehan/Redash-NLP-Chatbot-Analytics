from redashAPI import RedashAPIClient

api_key = '7uqzrON4MKNA1Zk7D4a7y9abgHZJ7PFB1WWQLsyZ'
api_url = "http://localhost:5001"
your_data_source_id = 1

Redash = RedashAPIClient(api_key, api_url)

def create_query(data_source_id: int, query: str, name: str, description: str="", options: dict=None):
    response = Redash.create_query(data_source_id, name, query, description, options)
    return {"status_code": response.status_code, "query_id": response.json()["id"]}


res = create_query(data_source_id=1, name="name", description="description", query="select * from cities_chart_data;")
print(res)
# Redash.create_query(1, "First Query", "SELECT * FROM table_name;")

# Redash.create_visualization(34, "line", "Second Visualization", x_axis="Date", y_axis=[
#     {"type": "line", "name": "Views", "label": "c2"}
# ])