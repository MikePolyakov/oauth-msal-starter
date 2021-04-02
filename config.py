class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # Enter your client secret from Azure AD below
    CLIENT_SECRET = "H4.4k.si0KLP.I8Fa1xX1A.jV7gIA~s92z"

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    # Enter your application client ID here
    CLIENT_ID = "63e32caf-0752-46a0-b7e3-6e89397a3a08"

    # Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL,
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session