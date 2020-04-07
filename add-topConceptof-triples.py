import rdflib

g = rdflib.Graph()

g.parse("nasa-competencies.ttl", format="ttl")

qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    CONSTRUCT { <urn:comp:0> skos:hasTopConcept ?x  }
       WHERE {
           { ?x a skos:Concept }
            FILTER NOT EXISTS { ?x skos:broader ?z }
       }""")

with open("addTopConceptOf.nt", "w") as output:
            output.write(qres.serialize(format='nt'))