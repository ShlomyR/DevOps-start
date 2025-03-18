targetScope = 'subscription'

param location string = 'Israel Central'
param resourceGroupName string = 'shlomyGroupTest'

resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: resourceGroupName
  location: location
}

module acrModule 'acr.bicep' = {
  name: 'deployACR'
  scope: rg
  params: {
    registryName: 'myUniqueACR' // Change this
    location: location
  }
}
