targetScope = 'resourceGroup'

param location string = 'Israel Central'
param registryName string = 'mydevopsacr'

resource acr 'Microsoft.ContainerRegistry/registries@2021-09-01' = {
  name: registryName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}
