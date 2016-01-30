########################   PROBABLY NOT NEEDED   ######################################

from saml2 import BINDING_HTTP_REDIRECT

CONFIG = \
    {
        "entityid": "http://saml.example.com:saml/idp.xml",
        "name": "MyMainServer",
        "service":
        {
            "idp":
            {
                "endpoints":
                {
                    "single_sign_on_service":
                        [("http://saml.example.com:saml:8088/sso",
                          BINDING_HTTP_REDIRECT)],
                    "single_logout_service":
                        [("http://saml.example.com:saml:8088/slo",
                          BINDING_HTTP_REDIRECT)]
                },
                "policy":
                {
                    "default":
                    {
                        "lifetime": {"minutes": 15},
                        "attribute_restrictions": None, # means all I have
                        "name_form": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
                    },
                    "urn:mace:example.com:saml:roland:sp":
                    {
                        "lifetime": {"minutes": 5},
                        "attribute_restrictions":
                        {
                            "givenName": None,
                             "surName": None,
                        }
                    }
                }
            }
            },
        "key_file": "my.key",
        "cert_file": "ca.pem",
        "xmlsec_binary": "/usr/local/bin/xmlsec1",
        "metadata":
            {
                "local": ["edugain.xml"],
            },
        "attribute_map_dir": "attributemaps"
    }
