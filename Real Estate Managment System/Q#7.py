class Property:
    def __init__(self, address, property_type, price):
        self.address = address
        self.property_type = property_type
        self.price = price
        self.available = True

class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.interested_properties = []

class Agent:
    def __init__(self, name, agent_id):
        self.name = name
        self.agent_id = agent_id
        self.listed_properties = []

class RealEstateAgency:
    def __init__(self):
        self.properties = []
        self.clients = []
        self.agents = []

    def add_property(self, property):
        self.properties.append(property)
        print(f"Address:{property.address}  Property Type:{property.property_type} Price: {property.price}$")

    def register_client(self, client):
        self.clients.append(client)
        print(f"Client Name: {client.name} Client-ID {client.client_id}")

    def assign_agent(self, agent):
        self.agents.append(agent)
        print(f"Agent Name: {agent.name} Agent-Id: {agent.agent_id}")


    def list_property(self, agent, property):
        agent.listed_properties.append(property)
        print(f" Name: {agent.name} Agent Id: {agent.agent_id}  Property:[Location: {property.address},{property.property_type}]")


    def express_interest(self, client, property):
        client.interested_properties.append(property)
        print(f"Client Name: {client.name} Client-Id: {client.client_id} interested to bought : {property.property_type} Location: {property.address}")

    def buy_property(self, client, property):
        if property.available:
            property.available = False
            print(f"{client.name} bought {property.property_type} in {property.address}")
        else:
            print("Property not available")

agency = RealEstateAgency()
property1 = Property("Islamabad Sector H-8/4,Street no 2 H#12 ","House",6000000)
property2 = Property("Islamabad Sector G-7/4, Street no 5 H#08","Plaza",300000000)
client1 = Client("Hassan Khawar","CLNT-21")
client2 = Client("M Khizar","CLNT-12")
agent1 = Agent("Asif Ali","AGN-32")
agent2 = Agent("Tariq Masud","AGN-21")
print("\t\t\t\t Add Property")
agency.add_property(property1)
agency.add_property(property2)
print("\t\t\t\t Agent For Properties")

agency.list_property(agent1,property1)
agency.list_property(agent2,property2)
print("\t\t\t\t\tClient Interest in Property")
agency.express_interest(client1,property1)
agency.express_interest(client2,property2)
print("\t\t\t\t\tClient Bought Property")
agency.buy_property(client1,property1)