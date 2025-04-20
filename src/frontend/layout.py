from dash import html, dcc

def get_layout():
    return html.Div([
        html.H1("Inventory Dashboard"),
        html.Div([
            html.Span("ID", style={"width": "100px", "display": "inline-block", "fontWeight": "bold"}),
            html.Span("Name", style={"width": "200px", "display": "inline-block", "fontWeight": "bold"}),
            html.Span("Quantity", style={"width": "100px", "display": "inline-block", "fontWeight": "bold"}),
            html.Span("Price", style={"width": "100px", "display": "inline-block", "fontWeight": "bold"}),
            html.Span("Category", style={"width": "100px", "display": "inline-block", "fontWeight": "bold"})
        ]),
        html.Div(id="items-table"),
        html.Button("Refresh Items", id="refresh-button", n_clicks=0),
        html.Hr(),
        html.H2("Add New Item"),
        html.Div([
            html.Label("Name:"),
            dcc.Input(id="name-input", type="text", value=""),
            html.Label("Quantity:"),
            dcc.Input(id="quantity-input", type="number", value=0),
            html.Label("Price:"),
            dcc.Input(id="price-input", type="number", value=0.0, step=0.01),
            html.Label("Category:"),
            dcc.Input(id="category-input", type="text", value=""),
            html.Button("Add Item", id="add-button", n_clicks=0),
            html.Div(id="add-output")
        ], style={"marginTop": "20px"})
    ])