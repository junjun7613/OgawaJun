#! /usr/bin/python
# coding = 'utf-8'

import xml, re
from bs4 import BeautifulSoup
from py2neo import Graph, Node, Relationship, NodeMatcher



url = "http://neo4j:caesar44310@localhost:7474/db/data/"
g = Graph("http://localhost:7474", username="neo4j", password="caesar44310")
#tx = g.begin()
matcher = NodeMatcher(g)


#XMLファイルから必要な情報を取得し、変数に格納

file1 = open('personlist.xml', 'rb')
file2 = open('placelist.xml', 'rb')


g.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r", data_contents=True)

soup_person = BeautifulSoup(file1, "lxml")
persons = soup_person.find_all("person")
for person in persons:
    person = person["xml:id"]
    key = person
    node_person = Node("Person", name=key)
    g.create(node_person)

soup_place = BeautifulSoup(file2, "lxml")
places = soup_place.find_all("place")
for place in places:
    related_place = place["xml:id"]
    key = related_place
    node_place = Node("Place", name=key)
    g.create(node_place)
    
#ここから関係性の構築
    
for pers in persons:
    pers_name = pers["xml:id"]
    traits = pers.find_all("trait")
    for trait in traits:
        relation = trait["type"]
        relation_item = trait["ana"]
        relation_item = relation_item.replace('#', '')
        relation_type = trait["subtype"]
        if relation_type == 'pers':
            existing_u1 = matcher.match('Person', name=pers_name).first()
            existing_u2 = matcher.match('Person', name=relation_item).first()
            existing_u1_knows_u2 = Relationship(existing_u1, relation, existing_u2)
            g.create(existing_u1_knows_u2)
        elif relation_type == 'plac':
            existing_u1 = matcher.match('Person', name=pers_name).first()
            existing_u2 = matcher.match('Place', name=relation_item).first()
            existing_u1_knows_u2 = Relationship(existing_u1, relation, existing_u2)
            g.create(existing_u1_knows_u2)
        else:
            pass

for plac in places:
    plac_name = plac["xml:id"]
    traits = plac.find_all("trait")
    for trait in traits:
        relation = trait["type"]
        relation_item = trait["ana"]
        relation_item = relation_item.replace('#', '')
        relation_type = trait["subtype"]
        if relation_type == 'pers':
            existing_u1 = matcher.match('Place', name=plac_name).first()
            existing_u2 = matcher.match('Person', name=relation_item).first()
            existing_u1_knows_u2 = Relationship(existing_u1, relation, existing_u2)
            g.create(existing_u1_knows_u2)
        elif relation_type == 'plac':
            existing_u1 = matcher.match('Place', name=plac_name).first()
            existing_u2 = matcher.match('Place', name=relation_item).first()
            existing_u1_knows_u2 = Relationship(existing_u1, relation, existing_u2)
            g.create(existing_u1_knows_u2)
        else:
            pass
        



            
        

    
    


