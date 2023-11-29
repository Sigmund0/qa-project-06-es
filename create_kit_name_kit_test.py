import sender_stand_request
import data

# Se define la función para pruebas positivas:
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Se define la función para pruebas negativas:
def negative_assert_code_400(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.token)
    assert kit_response.status_code == 400

# Test 1 El número permitido de caracter es (1)
def test_create_kit_1_letter_in_name_post_success_response():
    kit_body = data.kit_body_1_letter
    positive_assert(kit_body)

# Test 2 El número permitido de caracter es (511)
def test_create_kit_511_letter_in_name_post_success_response():
    kit_body = data.kit_body_511_letter
    positive_assert(kit_body)

# Test 3 El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_name_post_fail_response():
    kit_body = data.kit_body_0_letter
    negative_assert_code_400(kit_body)

# Test 4 El número de caracteres es superior al permitido (512)
def test_create_kit_512_letter_in_name_post_fail_response():
    kit_body = data.kit_body_512_letter
    negative_assert_code_400(kit_body)

# Test 5 Se permiten caracteres especiales
def test_create_kit_symbol_letter_in_name_post_success_response():
    kit_body = data.kit_body_symbol_letter
    positive_assert(kit_body)

# Test 6 Se permiten espacios
def test_create_kit_space_letter_in_name_post_success_response():
    kit_body = data.kit_body_space_letter
    positive_assert(kit_body)

# Test 7 Se permiten números
def test_create_kit_numbers_letter_in_name_post_success_response():
    kit_body = data.kit_body_numbers_letter
    positive_assert(kit_body)

# Test 8 El parámetro no se pasa en la solicitud:
def test_create_kit_nothing_letter_in_name_post_fail_response():
    kit_body = data.kit_body_nothing
    negative_assert_code_400(kit_body)

# Test 9 Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_incorrect_letter_in_name_post_fail_response():
    kit_body = data.kit_body_incorrect_letter
    negative_assert_code_400(kit_body)