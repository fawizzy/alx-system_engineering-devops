from datadog import initialize, api

options = {
    'api_key': 'e0d5e163eac3048ded56200f659163ae',
    'app_key': 'b729a6b515eca3f1df175d5e2bb93326a5e2aeec'
}

initialize(**options)

# print(options)

a = api.Dashboard.get_all()
# a = api.DashboardList.get(4741)
print(a)
