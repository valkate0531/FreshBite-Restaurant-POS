{
    "name": "FreshBite Restaurant POS",
    "summary": "FreshBite Restaurant branding for Odoo",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "license": "MIT",
    "author": "FreshBite Restaurant",
    "depends": ["point_of_sale", "web"],
    "data": [
        "views/branding_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "freshbite_pos/static/src/css/freshbite_theme.css",
        ],
        "web.assets_backend": [
            "freshbite_pos/static/src/css/freshbite_theme.css",
        ],
        "point_of_sale._assets_pos": [
            "freshbite_pos/static/src/css/freshbite_theme.css",
        ],
    },
    "installable": True,
    "application": False,
}
