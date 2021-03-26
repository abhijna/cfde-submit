import pytest
from globus_automate_client.flows_client import ALL_FLOW_SCOPES
from cfde_submit import client, exc


def test_logged_out(logged_out):
    assert client.CfdeClient().is_logged_in() is False


def test_logged_in(logged_in):
    assert client.CfdeClient().is_logged_in() is True


def test_scopes(mock_remote_config):
    cfde = client.CfdeClient()
    for service in ["dev", "staging", "prod"]:
        # Ensure all automate scopes are present
        cfde.service_instance = service
        assert not set(ALL_FLOW_SCOPES).difference(cfde.scopes)
        assert f'{service}_cfde_ep_id' in cfde.gcs_https_scope
        assert cfde.flow_scope == (f'https://auth.globus.org/scopes/'
                                   f'{service}_flow_id/flow_{service}_flow_id_user')


@pytest.mark.parametrize("config_setting", ["cfde_ep_id", "flow_id"])
def test_submissions_disabled(mock_remote_config, config_setting):
    """Test that a 'None' Value for either "cfde_ep_id" or "flow_id" disables
    submissions."""
    cfde = client.CfdeClient()
    cfde.service_instance = "prod"
    mock_remote_config.return_value["FLOWS"]["prod"][config_setting] = None
    with pytest.raises(exc.SubmissionsUnavailable):
        cfde.check()


def test_start_deriva_flow_while_logged_out(logged_out):
    with pytest.raises(exc.NotLoggedIn):
        client.CfdeClient().start_deriva_flow("path_to_executable.zip", "my_dcc")


def test_start_deriva_flow_http(logged_in, mock_validation, mock_remote_config, mock_flows_client,
                                mock_upload, mock_get_bag):
    mock_validation.return_value = "/home/cfde-user/bagged_path.zip"
    client.CfdeClient().start_deriva_flow("bagged_path.zip", "my_dcc")

    assert mock_validation.called
    assert mock_upload.called
    assert mock_flows_client.get_flow.called
    assert mock_flows_client.run_flow.called

    _, args, kwargs = mock_flows_client.run_flow.mock_calls[0]
    flow_id, flow_scope, flow_input = args
    assert flow_id == 'prod_flow_id'
    assert flow_scope == 'https://auth.globus.org/scopes/prod_flow_id/flow_prod_flow_id_user'
    assert flow_input == {
        'cfde_ep_id': 'prod_cfde_ep_id',
        'data_url': 'https://prod-gcs-inst.data.globus.org/CFDE/data/prod/bagged_path.zip',
        'dcc_id': 'my_dcc',
        'source_endpoint_id': False,
        'test_sub': False
    }


def test_start_deriva_flow_gcp(logged_in, mock_validation, mock_remote_config, mock_flows_client,
                               mock_upload, mock_gcp_installed, mock_get_bag):
    mock_validation.return_value = "/home/cfde-user/bagged_path.zip"
    client.CfdeClient().start_deriva_flow("bagged_path.zip", "my_dcc")

    assert mock_validation.called
    assert not mock_upload.called
    assert mock_flows_client.get_flow.called
    assert mock_flows_client.run_flow.called

    _, args, kwargs = mock_flows_client.run_flow.mock_calls[0]
    flow_id, flow_scope, flow_input = args
    assert flow_id == 'prod_flow_id'
    assert flow_scope == 'https://auth.globus.org/scopes/prod_flow_id/flow_prod_flow_id_user'
    assert flow_input == {
        'cfde_ep_id': 'prod_cfde_ep_id',
        'dcc_id': 'my_dcc',
        'source_endpoint_id': 'local_gcp_endpoint_id',
        'test_sub': False,
        'cfde_ep_path': '/CFDE/data/prod/bagged_path.zip',
        'cfde_ep_url': 'https://prod-gcs-inst.data.globus.org',
        'is_directory': False,
        'source_path': 'bagged_path.zip'
    }


def test_start_deriva_flow_force_http(logged_in, mock_validation, mock_remote_config,
                                      mock_flows_client, mock_upload, mock_gcp_installed,
                                      mock_get_bag):
    mock_validation.return_value = "/home/cfde-user/bagged_path.zip"
    client.CfdeClient().start_deriva_flow("bagged_path.zip", "my_dcc", force_http=True)
    assert mock_validation.called
    assert mock_upload.called
    assert mock_flows_client.get_flow.called
    assert mock_flows_client.run_flow.called


def test_client_invalid_version(logged_in, mock_remote_config):
    mock_remote_config.return_value["MIN_VERSION"] = "9.9.9"
    with pytest.raises(exc.OutdatedVersion):
        client.CfdeClient().check()


def test_client_permission_denied_404(logged_in, mock_remote_config, mock_flows_client,
                                      mock_globus_api_error):
    mock_globus_api_error.http_status = 404
    mock_flows_client.get_flow.side_effect = mock_globus_api_error
    with pytest.raises(exc.PermissionDenied):
        client.CfdeClient().check()


def test_client_permission_denied_405(logged_in, mock_remote_config, mock_flows_client,
                                      mock_globus_api_error):
    mock_globus_api_error.http_status = 405
    mock_flows_client.get_flow.side_effect = mock_globus_api_error
    with pytest.raises(exc.PermissionDenied):
        client.CfdeClient().check()
