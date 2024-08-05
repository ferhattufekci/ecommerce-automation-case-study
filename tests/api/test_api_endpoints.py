import requests

def test_token_endpoint():
    response = requests.post("http://localhost:5000/token", headers={"user": "user", "pass": "pass"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_view_invoice_endpoint():
    response = requests.get("http://localhost:5000/viewInvoice?barcode=12345")
    assert response.status_code == 200
    assert response.json() == {"InvoiceLink": "http://abc.com/invoice.pdf", "Result": {"success": True}}

def test_send_invoice_endpoint():
    token = requests.post("http://localhost:5000/token", headers={"user": "user", "pass": "pass"}).json()["token"]
    response = requests.post("http://localhost:5000/sendInvoice", headers={"token": token}, json={"Barcode": "12345"})
    assert response.status_code == 200