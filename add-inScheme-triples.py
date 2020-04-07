import rdflib

g = rdflib.Graph()

g.parse("nasa-competencies.ttl", format="ttl")

qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    CONSTRUCT { ?concept skos:inScheme <urn:comp:0> .  }
       WHERE {
           { ?concept a skos:Concept ;
             skos:broader ?broader .}
       }""")

with open("addInScheme.nt", "w") as output:
            output.write(qres.serialize(format='nt'))