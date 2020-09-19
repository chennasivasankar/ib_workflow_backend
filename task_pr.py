def create_task(no_of_tasks: int):
    import requests

    headers = {'Authorization': 'Bearer Eeg2cr9yizrBYtJHKlFE4aIu8z9MgG'}

    for i in range(no_of_tasks):
        data = {
            "task_gofs": [{
                "gof_id": "FIN_REQUESTOR_DETAILS",
                "same_gof_order": 0,
                "gof_fields": [{
                    "field_id": "FIN_TEAM_NAME",
                    "field_response": "Tech Team"
                }, {
                    "field_id": "FIN_PAYMENT_POC_NAME",
                    "field_response": "65715597-e66b-4826-a74a-d831461906d5"
                }, {
                    "field_id": "FIN_PAYMENT_REQUESTOR_NAME",
                    "field_response": "Plain Text"
                }, {
                    "field_id": "FIN_PAYMENT_APPROVER_NAME",
                    "field_response": "be0bda03-4425-4060-982b-6a5e5356840d"
                }]
            }, {
                "gof_id": "FIN_TIMELINE_PRIORITY",
                "same_gof_order": 0,
                "gof_fields": [{
                    "field_id": "FIN_PAYMENT_REQUEST_DATE",
                    "field_response": "2000-02-20"
                }, {
                    "field_id": "FIN_TENTATIVE_PAYMENT_DATE",
                    "field_response": "2000-02-20"
                }, {
                    "field_id": "FIN_EXPECTED_PAYMENT_TIMELINE",
                    "field_response": "Standard Timeline"
                }, {
                    "field_id": "FIN_PRIORITY",
                    "field_response": "Critical - Confirmed by Sir"
                }, {
                    "field_id": "FIN_EXPECTED_PAYMENT_TIMELINE_REMARKS",
                    "field_response": "In computing, plain text is a loose term for data that represent only characters of readable material but not its graphical representation nor other objects. I"
                }]
            }, {
                "gof_id": "FIN_PAYMENT_TYPE",
                "same_gof_order": 0,
                "gof_fields": [{
                    "field_id": "FIN_TYPE_OF_PAYMENT_REQUEST",
                    "field_response": "Vendor Payment"
                }, {
                    "field_id": "FIN_COMPANY_NAME",
                    "field_response": "iBuild"
                }]
            }, {
                "gof_id": "FIN_VENDOR_PAYMENT_DETAILS",
                "same_gof_order": 0,
                "gof_fields": [{
                    "field_id": "FIN_VENDOR_NAME",
                    "field_response": "Vendor 1"
                }, {
                    "field_id": "FIN_PURPOSE_OF_THE_EXPENSE",
                    "field_response": "Plain Text"
                }, {
                    "field_id": "FIN_PAYMENT_TYPE_VENDOR",
                    "field_response": "One Time Payment"
                }, {
                    "field_id": "FIN_PAYMENT_MODE_VENDOR",
                    "field_response": "Online Payment"
                }, {
                    "field_id": "FIN_CURRENCY_VENDOR",
                    "field_response": "AFN - Afghan afghani"
                }, {
                    "field_id": "FIN_INVOICE_AMOUNT",
                    "field_response": 1.2
                }, {
                    "field_id": "FIN_REQUESTED_AMOUNT",
                    "field_response": 1.2
                }, {
                    "field_id": "FIN_CONVERSION_RATE_VENDOR",
                    "field_response": 1.2
                }, {
                    "field_id": "FIN_REQUESTED_AMOUNT_AFTER_CONVERSION",
                    "field_response": 1.2
                }]
            }, {
                "gof_id": "FIN_VENDOR_ONLINE_EXPENSE_TYPE",
                "same_gof_order": 0,
                "gof_fields": [{
                    "field_id": "FIN_CATEGORY_ONLINE_EXPENSE",
                    "field_response": "Plain Text"
                }, {
                    "field_id": "FIN_EVENTS_ACTIVITY_ONLINE_EXPENSE",
                    "field_response": "Entrepreneurship talk in Bundelkhand Chamber of Commerce & Industry"
                }, {
                    "field_id": "FIN_PRODUCT_SERVICE",
                    "field_response": "Product"
                }]
            }, {
                "gof_id": "FIN_GST_DETAILS",
                "same_gof_order": 0,
                "gof_fields": [{
                    "field_id": "FIN_GST_OFFICE_LOCATION",
                    "field_response": "Plain Text"
                }, {
                    "field_id": "FIN_GST_LOCATION",
                    "field_response": "7"
                }, {
                    "field_id": "FIN_GST_NUMBER",
                    "field_response": "Plain Text"
                }, {
                    "field_id": "FIN_GST_ADDRESS",
                    "field_response": "Plain Text"
                }]
            }, {
                "gof_id": "FIN_ATTACHMENTS_INVOICE",
                "same_gof_order": 0,
                "gof_fields": [{
                    "field_id": "FIN_SOFT_COPY_STATUS",
                    "field_response": "Uploaded"
                }, {
                    "field_id": "FIN_TYPE_OF_ATTACHMENT",
                    "field_response": "https://cdn.zeplin.io/5efacaf3a9674a242eb8fb11/assets/b14964e2-56ae-47d4-a4c9-df3f84cf1064.png"
                }, {
                    "field_id": "FIN_ATTACHMENT",
                    "field_response": "https://cdn.zeplin.io/5efacaf3a9674a242eb8fb11/assets/b14964e2-56ae-47d4-a4c9-df3f84cf1064.png"
                }, {
                    "field_id": "FIN_TAX_INVOICE_UPLOAD_DATE",
                    "field_response": "2000-02-20"
                }, {
                    "field_id": "FIN_TAX_INVOICE_SUBMISSION_REMARKS",
                    "field_response": "In computing, plain text is a loose term for data that represent only characters of readable material but not its graphical representation nor other objects. I"
                }, {
                    "field_id": "FIN_HARD_COPY_SUBMISSION_STATUS",
                    "field_response": "Submitted"
                }, {
                    "field_id": "FIN_HARD_COPY_REMARKS",
                    "field_response": "In computing, plain text is a loose term for data that represent only characters of readable material but not its graphical representation nor other objects. I"
                }, {
                    "field_id": "FIN_HARD_COPY_COURIER_FROM_LOCATION",
                    "field_response": ""
                }, {
                    "field_id": "FIN_HARD_COPY_SUBISSION_DATE",
                    "field_response": "2000-02-20"
                }, {
                    "field_id": "FIN_HARD_COPY_REFERENCE_ID",
                    "field_response": "Plain Text"
                }]
            }],
            "project_id": "FIN_MAN",
            "task_template_id": "FIN_PR",
            "action_id": 40,
            "title": "Payment Request 1",
            "description": "",
            "start_datetime": "2019-01-01 01:02:33",
            "due_datetime": "2020-10-02 01:02:33",
            "priority": "MEDIUM"
        }
        response = requests.post(
            "https://dd5d9fb7bf83.ngrok.io/api/ib_tasks/task/v1/",
            headers=headers, json=data)
