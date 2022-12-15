# Django-Coding-Test
steps
1. Pull latest from this repo

2. Install poetry in your pc (dont't install if already installed). If dont't want to use poetry then setup a classical Virtual environment and install dependency from requirements.txt provided (In src directory).

3. Run "poetry install" to install all dependency.(It will create virtual environment automatically)

4. To generate requirements.txt run "poetry export --without-hashes -f requirements.txt --output requirements.txt" this in src directory.

5. To run project run "poetry run python manage.py runserver" or "poetry shell" to activate poetry virtual environment and then run normal python commands to run the project.


**** All Steps are completed ****

N.B:
    1. Step create product and edit product are completed only with postman test because I don't know frontend so much.
    2. I am only a beckend developer and not full-stack.
    3. I tried to run vue.js version of this test project with node version   14, 16, 18 but ended with some kind of error.
    4. Tested postman body data are given below.


* create product body sample data:
{
    "product":{
        "title": "Alcohol Pad",
        "sku": "ACP53531",
        "description": "Product details of 100 PCS / 1 BOX Alcohol Pad Non Woven Material (Viscose, Polyester) Saturated With Isopropyl Alcohol 70% Direction: Cleaning Required The Area, Discar After Single Use.Suitable For Skin Cleaning Prior To Subcutaneous Injections And The Taking Of Capillary Blood Samples. Pack Of 100 Outside: 50Mm X 50Mm Inside:35Mm X 35MmNon Woven Material (Viscose, Polyester) Saturated With Isopropyl Alcohol 70% , Suitable For Skin Cleaning Prior To Subcutaneous Injections And The Taking Of Capillary Blood Samples. Direction: Cleaning Required The Area, Discard After Single Use. Outside: 50Mm X 50Mm Inside:35Mm X 35Mm."
    },
	"product_image": "https://static-01.daraz.com.bd/p/ca2446802a54c7f268e1639118ec97c8.png",
	"product_variants": [
        {
            "product_variant_one": {
                "variant": "Size",
                "variant_title":"x" 
            },
            "product_variant_two": {
                "variant": "Color",
                "variant_title":"blue" 
            },
            "price": 200,
            "stock": 500
        },
        {
            "product_variant_one": {
                "variant": "Size",
                "variant_title":"x" 
            },
            "product_variant_two": {
                "variant": "Color",
                "variant_title":"blue" 
            },
            "product_variant_three": {
                "variant": "Style",
                "variant_title":"round" 
            },
            "price": 410,
            "stock": 5000
        }
    ]
	
}

* update product body sample data:
{
    "product":{
        "title": "Alcohol Pad",
        "sku": "ACP53531",
        "description": "Product details of 100 PCS / 1 BOX Alcohol Pad Non Woven Material (Viscose, Polyester) Saturated With Isopropyl Alcohol 70% Direction: Cleaning Required The Area, Discar After Single Use.Suitable For Skin Cleaning Prior To Subcutaneous Injections And The Taking Of Capillary Blood Samples. Pack Of 100 Outside: 50Mm X 50Mm Inside:35Mm X 35MmNon Woven Material (Viscose, Polyester) Saturated With Isopropyl Alcohol 70% , Suitable For Skin Cleaning Prior To Subcutaneous Injections And The Taking Of Capillary Blood Samples. Direction: Cleaning Required The Area, Discard After Single Use. Outside: 50Mm X 50Mm Inside:35Mm X 35Mm."
    },
	
	"product_variants_price": [
        {
            "pk":1, 
            "price": 200,
            "stock": 500
        },
        {
            "pk": 2,
            "price": 410,
            "stock": 5000
        }
    ]
	
}