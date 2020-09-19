
def create_task():
	import requests

	headers = {'Authorization': 'Bearer pqwOUZvk3DhHYmSyA6URhcL0eEmO3r'}

	data = {
		"task_gofs": [{
			"gof_id": "FIN_ADDRESS_DETAILS",
			"same_gof_order": 0,
			"gof_fields": [{
				"field_id": "FIN_ADDRESS_LINE_1",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_ADDRESS_LINE_2",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_CITY",
				"field_response": "14"
			}, {
				"field_id": "FIN_STATE",
				"field_response": "8"
			}, {
				"field_id": "FIN_COUNTRY",
				"field_response": "9"
			}, {
				"field_id": "FIN_PINCODE",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_MOBILE/PHONE",
				"field_response": "9515954395"
			}, {
				"field_id": "FIN_FAX",
				"field_response": "Plain Text"
			}]
		}, {
			"gof_id": "FIN_BANK_DETAILS",
			"same_gof_order": 0,
			"gof_fields": [{
				"field_id": "FIN_BANK_DETAILS_PROOF",
				"field_response": "https://cdn.zeplin.io/5efacaf3a9674a242eb8fb11/assets/b14964e2-56ae-47d4-a4c9-df3f84cf1064.png"
			}, {
				"field_id": "FIN_ACCOUNT_NUMBER",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_BENEFICIARY_NAME",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_BENIFICIARY_BANK_NAME",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_IFSC_CODE",
				"field_response": "Plain Text"
			}]
		}, {
			"gof_id": "FIN_GOF_VENDOR_TYPE",
			"same_gof_order": 0,
			"gof_fields": [{
				"field_id": "FIN_TYPE_OF_VENDOR",
				"field_response": "Individual"
			}]
		}, {
			"gof_id": "FIN_VENDOR_BASIC_DETAILS",
			"same_gof_order": 0,
			"gof_fields": [{
				"field_id": "FIN_SALUATION",
				"field_response": "Mr."
			}, {
				"field_id": "FIN_FIRST_NAME",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_LAST_NAME",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_DISPLAY_NAME",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_EMAIL",
				"field_response": "muneera@gmail.com"
			}, {
				"field_id": "FIN_PHONE",
				"field_response": "9515954395"
			}, {
				"field_id": "FIN_WEBSITE",
				"field_response": "https://ibcom.ibhubs.co/ibhubs/channels/ib-devs-team3"
			}]
		}, {
			"gof_id": "FIN_GST&TDS_TYPE",
			"same_gof_order": 0,
			"gof_fields": [{
				"field_id": "FIN_GST_REGISTRATION_TYPE",
				"field_response": "Registered Business - Regular"
			}]
		}, {
			"gof_id": "FIN_GST&TDS_DETAILS",
			"same_gof_order": 0,
			"gof_fields": [{
				"field_id": "FIN_GSTIN/UIN",
				"field_response": "Plain Text"
			}, {
				"field_id": "FIN_GST_CERTIFICATE",
				"field_response": "https://cdn.zeplin.io/5efacaf3a9674a242eb8fb11/assets/b14964e2-56ae-47d4-a4c9-df3f84cf1064.png"
			}, {
				"field_id": "FIN_TAX_PAYER_TYPE",
				"field_response": "Regular"
			}, {
				"field_id": "FIN_GST_FILING_FREQUENCY",
				"field_response": "Monthly"
			}, {
				"field_id": "FIN_MSME_REGISTERED",
				"field_response": "Registered"
			}, {
				"field_id": "FIN_MSME_CERTIFICATE",
				"field_response": "https://cdn.zeplin.io/5efacaf3a9674a242eb8fb11/assets/b14964e2-56ae-47d4-a4c9-df3f84cf1064.png"
			}, {
				"field_id": "FIN_CURRENCY",
				"field_response": "INR"
			}, {
				"field_id": "FIN_PAYMENT_TERMS",
				"field_response": "Due end of Month"
			}]
		}],
		"project_id": "FIN_MAN",
		"task_template_id": "FIN_VENDOR",
		"action_id": 50,
		"title": "Victory Celebrations",
		"description": "",
		"start_datetime": "2020-9-9 0:0:0",
		"due_datetime": "2020-9-30 0:0:0",
		"priority": "MEDIUM"
	}
	requests.post("http://127.0.0.1:1513/api/ib_tasks/task/v1/", headers=headers, json=data)





































