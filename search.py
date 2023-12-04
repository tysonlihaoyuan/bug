

import json
import csv
from pandas import*
import requests

data={
    "id": 6280,
    "uuid": "5890c43a-fe11-4c84-b38a-6f8d461801e1",
    "name": "PROMETAL",
    "address": {
        "id": 6345,
        "street": "56 rue Durette",
        "city": "Matane",
        "province": "Québec",
        "postal_code": "G4W 0J6",
        "country": "Canada",
        "longitude": "-67.565840",
        "latitude": "48.835210"
    },
    "phone_number": "418-562-2295",
    "website": "http://www.prometalinc.ca/",
    "description": "Soudure générale, fabrication de structures d’acier, de métaux ouvrés et de mécano-soudé.",
    "picture": "https://grad4-static-data.s3.amazonaws.com/image/company/LOGO__CWB_version_2_petit.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=0c6114f720eaaf90386ee238c43c33122982ea0b50489a11a18c305546a871cb",
    "number_employee": 12,
    "shop_floor_area": "5200",
    "subscribed_to_companies": [
        {
            "id": 5001,
            "uuid": "4389b004-e050-4839-b920-2cb6f1c0a947",
            "name": "Hydro-Québec",
            "is_online": "false",
            "last_seen": "2023-09-06T09:28:22",
            "picture": "https://grad4-static-data.s3.amazonaws.com/media/companies/5001/logo.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=db8c6269c57fbcfbd581d7db1460321bab35e1ac75dd03b2d60eaebfd6422fdd"
        }
    ],
    "is_claimed": 'true',
    "references": [],
    "past_projects_pictures": [
        {
            "id": 11265,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_0312.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=578f27512806c2b8e76bfe5f108ce989207e4dab26d40ca6d5fc73d3b48f51e5"
        },
        {
            "id": 11266,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_0339.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=87a1f6300947ce1001af5d94f4879bc801779c255b839b817672e0bff47a974c"
        },
        {
            "id": 11267,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_1032.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d8407b92ca35a947c091013ce6c1ada6e098bf622166ca84f9fdc1795fbf06e1"
        },
        {
            "id": 11268,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_1377.JPG?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=e6be16c61e856eacd9d8ef2a53257eb3cfd8258faa761230d971f6d2ffc813f2"
        },
        {
            "id": 11269,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_1599.JPG?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=342f51deb749546ed02b29baa0e96e6462ab12fecd344773bd798abb10b9c33b"
        },
        {
            "id": 11270,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_1849.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d9f12b03d652499749e7dd45307c5c716700c572d2436827594f939f17d254f4"
        },
        {
            "id": 11271,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_2603.JPG?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=c0a2a73acf7d4687d1292f4b6493a013f5dd940fdb6c70a356d476ae1f3a3bfa"
        },
        {
            "id": 11272,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/IMG_2630.JPG?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=5dc1507dbb5e009be7a96b393d17087919edff136cbc6e40ca670b68a5201c35"
        }
    ],
    "shop_pictures": [
        {
            "id": 11264,
            "url": "https://grad4-static-data.s3.amazonaws.com/company_images/326198243_589956952967788_853705204563610579_n.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=120da8160d76f40f2130a5dbacde6bbc76f84a04e7f91c0c79d3ae5f2371df9e"
        }
    ],
    "documents": [],
    "additional_details": "Installée depuis plus de 12 ans dans le parc industriel de Matane, l’entreprise Prométal Inc. est un fabricant employant une vingtaine d’employés qui réalise des produits sur mesure pour l’industrie de la construction commerciale, industrielle et institutionnelle. L’entreprise œuvre en soudure générale, fabrication de structures d’acier, de métaux ouvrés et de mécano-soudé, en plus d’offrir un service d’unités mobiles.\r\nNouvellement entièrement rénovée et à la fine pointe de la technologie, Prométal est une usine d’une superficie de 483 mètres carrés (5 200 pieds carrés) et d’une hauteur de 20 pi. Elle a également des bureaux adjacents de 185 mètres carrés (2 000 pieds carrés).\r\nPar ailleurs, Prométal offre des projets clé en main, allant de l’estimation à la livraison. Nous offrons également le service d’ingénierie, la conception de dessins d’ateliers et les prises de mesures scan 3D.\r\nAussi, l’entreprise propose aux fabricants de structures d’acier, des heures de fabrication lorsqu’ils font face à des échéanciers trop serrés ou des types de travaux hors de leurs standards. Pour ce faire, elle s’appuie sur une équipe solide, jeune, dynamique et professionnelle.\r\nL’entreprise dispose de tous les équipements nécessaires à la prise en charge rapide et la livraison juste à temps du produit pour assurer un contrôle très serré de la qualité et des échéanciers. Pour répondre à la demande sans cesse croissante du marché, ses installations des plus diversifiées incluent : 2 ponts-roulant d'une capacité de 5t, un chariot-élévateur de 10 000 lbs et un de 22 000 lbs, une presse-plieuse de 250 tonnes, 3 lignes de débitage avec scie à ruban 2436 et 9-18 dont une automatique, un sheer à plaques d’une capacité de 10 pi x 3/8, une table à découpe 6x12 d'une capacité de 1 1/2'' d'épaisseur, 10 postes de soudage, une ferrailleuse de 100 tonnes en plus d’un département de peinture primaire. L’usine a donc une grande capacité de production de métaux ouvrés et de structure d'acier.\r\nDe ce fait, Prométal inc. est prêt à vous offrir ses services en tant que sous-traitant afin de vous aider à livrer vos projets.",
    "additional_details_rich_text": "{\"blocks\":[{\"key\":\"asit1\",\"text\":\"Installée depuis plus de 12 ans dans le parc industriel de Matane, l’entreprise Prométal Inc. est un fabricant employant une vingtaine d’employés qui réalise des produits sur mesure pour l’industrie de la construction commerciale, industrielle et institutionnelle. L’entreprise œuvre en soudure générale, fabrication de structures d’acier, de métaux ouvrés et de mécano-soudé, en plus d’offrir un service d’unités mobiles.\",\"type\":\"unstyled\",\"depth\":0,\"inlineStyleRanges\":[],\"entityRanges\":[],\"data\":{}},{\"key\":\"cf1v0\",\"text\":\"Nouvellement entièrement rénovée et à la fine pointe de la technologie, Prométal est une usine d’une superficie de 483 mètres carrés (5 200 pieds carrés) et d’une hauteur de 20 pi. Elle a également des bureaux adjacents de 185 mètres carrés (2 000 pieds carrés).\",\"type\":\"unstyled\",\"depth\":0,\"inlineStyleRanges\":[],\"entityRanges\":[],\"data\":{}},{\"key\":\"e9u1c\",\"text\":\"Par ailleurs, Prométal offre des projets clé en main, allant de l’estimation à la livraison. Nous offrons également le service d’ingénierie, la conception de dessins d’ateliers et les prises de mesures scan 3D.\",\"type\":\"unstyled\",\"depth\":0,\"inlineStyleRanges\":[],\"entityRanges\":[],\"data\":{}},{\"key\":\"4725c\",\"text\":\"Aussi, l’entreprise propose aux fabricants de structures d’acier, des heures de fabrication lorsqu’ils font face à des échéanciers trop serrés ou des types de travaux hors de leurs standards. Pour ce faire, elle s’appuie sur une équipe solide, jeune, dynamique et professionnelle.\",\"type\":\"unstyled\",\"depth\":0,\"inlineStyleRanges\":[],\"entityRanges\":[],\"data\":{}},{\"key\":\"e6oni\",\"text\":\"L’entreprise dispose de tous les équipements nécessaires à la prise en charge rapide et la livraison juste à temps du produit pour assurer un contrôle très serré de la qualité et des échéanciers. Pour répondre à la demande sans cesse croissante du marché, ses installations des plus diversifiées incluent : 2 ponts-roulant d'une capacité de 5t, un chariot-élévateur de 10 000 lbs et un de 22 000 lbs, une presse-plieuse de 250 tonnes, 3 lignes de débitage avec scie à ruban 2436 et 9-18 dont une automatique, un sheer à plaques d’une capacité de 10 pi x 3/8, une table à découpe 6x12 d'une capacité de 1 1/2'' d'épaisseur, 10 postes de soudage, une ferrailleuse de 100 tonnes en plus d’un département de peinture primaire. L’usine a donc une grande capacité de production de métaux ouvrés et de structure d'acier.\",\"type\":\"unstyled\",\"depth\":0,\"inlineStyleRanges\":[],\"entityRanges\":[],\"data\":{}},{\"key\":\"4aeu1\",\"text\":\"De ce fait, Prométal inc. est prêt à vous offrir ses services en tant que sous-traitant afin de vous aider à livrer vos projets.\",\"type\":\"unstyled\",\"depth\":0,\"inlineStyleRanges\":[],\"entityRanges\":[],\"data\":{}}],\"entityMap\":{}}",
    "requires_consolidated_report": 'false',
    "plan_name": "premium",
    "email": "joey.cote@prometalinc.com",
    "employees_count": 12,
    "certificates": [
        {
            "name": " CSA W47.1",
            "file": {
                "file_name": "PRMEM1-W471-PROMTALINC-LOV",
                "file_extension": "pdf",
                "file_url": "https://grad4-static-data.s3.amazonaws.com/capabilities/PRMEM1-W471-PROMTALINC-LOV.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2RFSOPTN3OPPY3UA%2F20231202%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20231202T053615Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=792a0ed9fe4484f99c20b8448a42fc673f266d3f3392d94a27884c390c26d247"
            }
        }
    ],
    "expertise": [
        "Laser cutting",
        "Plasma cutting",
        "Bending",
        "Simple welding ( Welding station for small jobs )",
        "Welded assemblies",
        "Large size welded assemblies  ( Dim. > 5' x 5' )",
        "Laser tube",
        "Generic internal painting (Spray gun or others )",
        "Rolling",
        "Large size bending ( L >=8' )",
        "Large size cutting ( L >=9' )",
        "Laser cutting 3+ axis (Ex : cutting an edge at 45deg.",
        "Engineering design service (CAD)",
        "Turnkey full mechanical assembly",
        "Heat treatment"
    ],
    "ratings": 'null',
    "stats": {},
    "testimonials": [],
    "industry_expertise": [
        "Construction & Civil Engineering",
        "Energy Sector",
        "Forestry",
        "Governmental",
        "Industrial Equipment",
        "Mining",
        "Naval",
        "Oil And Gas",
        "Pulp And Paper Industry"
    ],
    "claimed": 'true',
    "is_premium": 'true',
    "profile_completeness": {
        "company_info": {
            "weightage": 20,
            "is_complete": 'true'
        },
        "manufacturing_capabilities": {
            "weightage": 20,
            "is_complete": 'true'
        },
        "certifications": {
            "weightage": 10,
            "is_complete": 'true'
        },
        "industry_expertise": {
            "weightage": 10,
            "is_complete": 'true'
        },
        "shop_pictures": {
            "weightage": 15,
            "is_complete": 'false'
        },
        "past_project_pictures": {
            "weightage": 15,
            "is_complete": 'true'
        },
        "documents": {
            "weightage": 10,
            "is_complete": 'false'
        },
        "total": 75
    }
}
def getSupplieFinalResult(data,hearderAuth):
    suppliers_csv=read_csv("buyer.csv")
    suppliersIds=suppliers_csv['id'].tolist()
    print(suppliersIds)
    searchSupplier_url="https://app.axya.co/api/v1/supplierProfile/"
    # print(type(suppliersIds[]))
    result = []
    for id in suppliersIds:
        searchSupplier_url_target=searchSupplier_url+str(id)
        supplier_search_response=requests.get(url=searchSupplier_url_target,headers=hearderAuth)

        supplier_search_data = json.loads(supplier_search_response.text)

        dic1={}
        dic1['name']=supplier_search_data.get('name')
        dic1['phone_number']=supplier_search_data.get('phone_number')
        dic1['website']=supplier_search_data.get('website')
        dic1['email']=supplier_search_data.get('email')
        dic1['country']=supplier_search_data['address'].get('country')
        dic1['city']=supplier_search_data['address'].get('city')
        dic1['street']=supplier_search_data['address'].get('street')
        result.append(dic1)
    
    

   

    # print(result)

def main():
    getSupplieFinalResult(data)

if __name__ == "__main__":
    main()

