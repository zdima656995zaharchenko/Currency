def test_get_contact_us(client):
    response = client.get('/contactus/create/')
    assert response.status_code == 200

def test_post_contact_us_empty_form(client):
    response = client.post('/contactus/create/')
    assert response.status_code == 200



def test_post_contact_us_empty_form_errors(client):
    response = client.post('/contactus/create/')
    assert response.context_data['form'].errors == {
        'name': ['This field is required.'],
        'reply_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.'],
    }

def test_post_contact_us_invalid_reply_to_200(client):
    payload = {
        'name': 'Name',
        'reply_to': 'INVALID_EMAIL',
        'subject': 'Subject',
        'body': 'Body'
    }
    response = client.post('/currency/contactus/create', data=payload )
    assert response.context_data['form'].errors == {
        'reply_to': ['Enter a valid email address.']
    }