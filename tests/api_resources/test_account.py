import xpay


TEST_RESOURCE_ID = "acct_123"
TEST_CAPABILITY_ID = "acap_123"
TEST_EXTERNALACCOUNT_ID = "ba_123"
TEST_PERSON_ID = "person_123"


class TestAccount(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Account.list()
        request_mock.assert_requested("get", "/v1/accounts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Account)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Account.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Account)

    def test_is_creatable(self, request_mock):
        resource = xpay.Account.create(country="US", type="custom")
        request_mock.assert_requested("post", "/v1/accounts")
        assert isinstance(resource, xpay.Account)

    def test_is_saveable(self, request_mock):
        account = xpay.Account.retrieve(TEST_RESOURCE_ID)
        account.metadata["key"] = "value"
        resource = account.save()
        request_mock.assert_requested(
            "post", "/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Account)
        assert resource is account

    def test_is_saveable_with_individual(self, request_mock):
        individual = xpay.Person.construct_from(
            {"id": "person_123", "object": "person", "first_name": "Jenny"},
            xpay.api_key,
        )
        account = xpay.Account.construct_from(
            {"id": "acct_123", "object": "account", "individual": individual},
            xpay.api_key,
        )

        account.individual.first_name = "Jane"

        request_mock.stub_request(
            "post",
            "/v1/accounts/%s" % TEST_RESOURCE_ID,
            account.to_dict_recursive(),
        )
        resource = account.save()
        request_mock.assert_requested(
            "post",
            "/v1/accounts/%s" % TEST_RESOURCE_ID,
            {"individual": {"first_name": "Jane"}},
        )
        assert isinstance(resource, xpay.Account)
        assert resource is account

    def test_is_modifiable(self, request_mock):
        resource = xpay.Account.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Account)

    def test_is_deletable(self, request_mock):
        resource = xpay.Account.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = xpay.Account.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_retrieve_no_id(self, request_mock):
        resource = xpay.Account.retrieve()
        request_mock.assert_requested("get", "/v1/account")
        assert isinstance(resource, xpay.Account)

    def test_can_reject(self, request_mock):
        account = xpay.Account.retrieve(TEST_RESOURCE_ID)
        resource = account.reject(reason="fraud")
        request_mock.assert_requested(
            "post",
            "/v1/accounts/%s/reject" % TEST_RESOURCE_ID,
            {"reason": "fraud"},
        )
        assert isinstance(resource, xpay.Account)
        assert resource is account

    def test_can_reject_classmethod(self, request_mock):
        resource = xpay.Account.reject(TEST_RESOURCE_ID, reason="fraud")
        request_mock.assert_requested(
            "post",
            "/v1/accounts/%s/reject" % TEST_RESOURCE_ID,
            {"reason": "fraud"},
        )
        assert isinstance(resource, xpay.Account)

    def test_is_deauthorizable(self, request_mock):
        account = xpay.Account.retrieve(TEST_RESOURCE_ID)
        request_mock.stub_request(
            "post", "/oauth/deauthorize", {"xpay_user_id": account.id}
        )
        account.deauthorize()
        request_mock.assert_requested(
            "post",
            "/oauth/deauthorize",
            {"client_id": xpay.client_id, "xpay_user_id": account.id},
        )

    def test_can_call_persons(self, request_mock):
        account = xpay.Account.retrieve(TEST_RESOURCE_ID)
        resources = account.persons()
        request_mock.assert_requested(
            "get", "/v1/accounts/%s/persons" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Person)


class TestAccountCapabilities(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Account.list_capabilities(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/accounts/%s/capabilities" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Capability)

    def test_is_modifiable(self, request_mock):
        resource = xpay.Account.modify_capability(
            TEST_RESOURCE_ID, TEST_CAPABILITY_ID, requested=True
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/%s/capabilities/%s"
            % (TEST_RESOURCE_ID, TEST_CAPABILITY_ID),
        )
        assert isinstance(resource, xpay.Capability)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Account.retrieve_capability(
            TEST_RESOURCE_ID, TEST_CAPABILITY_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/%s/capabilities/%s"
            % (TEST_RESOURCE_ID, TEST_CAPABILITY_ID),
        )
        assert isinstance(resource, xpay.Capability)


class TestAccountExternalAccounts(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Account.list_external_accounts(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/accounts/%s/external_accounts" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Account.retrieve_external_account(
            TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/%s/external_accounts/%s"
            % (TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID),
        )
        assert isinstance(resource, xpay.BankAccount)

    def test_is_creatable(self, request_mock):
        resource = xpay.Account.create_external_account(
            TEST_RESOURCE_ID, external_account="btok_123"
        )
        request_mock.assert_requested(
            "post", "/v1/accounts/%s/external_accounts" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.BankAccount)

    def test_is_modifiable(self, request_mock):
        resource = xpay.Account.modify_external_account(
            TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/%s/external_accounts/%s"
            % (TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID),
        )
        assert isinstance(resource, xpay.BankAccount)

    def test_is_deletable(self, request_mock):
        resource = xpay.Account.delete_external_account(
            TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID
        )
        request_mock.assert_requested(
            "delete",
            "/v1/accounts/%s/external_accounts/%s"
            % (TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID),
        )
        assert resource.deleted is True


class TestAccountLoginLinks(object):
    def test_is_creatable(self, request_mock):
        resource = xpay.Account.create_login_link(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/accounts/%s/login_links" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.LoginLink)


class TestAccountPersons(object):
    def test_is_creatable(self, request_mock):
        resource = xpay.Account.create_person(
            TEST_RESOURCE_ID, dob={"day": 1, "month": 1, "year": 1980}
        )
        request_mock.assert_requested(
            "post", "/v1/accounts/%s/persons" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Person)

    def test_is_deletable(self, request_mock):
        resource = xpay.Account.delete_person(
            TEST_RESOURCE_ID, TEST_PERSON_ID
        )
        request_mock.assert_requested(
            "delete",
            "/v1/accounts/%s/persons/%s" % (TEST_RESOURCE_ID, TEST_PERSON_ID),
        )
        assert resource.deleted is True

    def test_is_listable(self, request_mock):
        resources = xpay.Account.list_persons(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/accounts/%s/persons" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Person)

    def test_is_modifiable(self, request_mock):
        resource = xpay.Account.modify_person(
            TEST_RESOURCE_ID, TEST_PERSON_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/accounts/%s/persons/%s" % (TEST_RESOURCE_ID, TEST_PERSON_ID),
        )
        assert isinstance(resource, xpay.Person)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Account.retrieve_person(
            TEST_RESOURCE_ID, TEST_PERSON_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/accounts/%s/persons/%s" % (TEST_RESOURCE_ID, TEST_PERSON_ID),
        )
        assert isinstance(resource, xpay.Person)
