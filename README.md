# Shop-Generator
A program to generate custom Fortnite Item Shops - Specifically made for [Neonite](https://github.com/NeoniteDev/NeoniteV2).
This program is inspired by the Shop Generator by [InTheShade](https://github.com/OutTheShade)

# Requirements
- [requests](https://pypi.org/project/requests/)

# Features
- Custom Item Shop generation with multiple items, sets, + more
- Item shop generation of the newest cosmetics within the latest Fortnite Version
- Custom bundle generation
- Existing set shop generation
- Existing item bundle shop generation
- Generation in under a second
- Paid bundle support

# How-To-Use
Where to put data:
```jsonc

{
      "refreshIntervalHrs": 1,
      "dailyPurchaseHrs": 24,
      "expiration": "2040-09-21T11:00:00.000Z",
      "storefronts": [
          {
              "name": "BRStarterKits",
              "catalogEntries": [
                  // Put paid bundles here
              ]
          },

          {
              "name": "BRDailyStorefront",
              "catalogEntries":[
                  // Put normal items/bundles here
              ]
          }

      ]
}
```

Example of shop generation:

```jsonc

{
  "refreshIntervalHrs": 1,
  "dailyPurchaseHrs": 24,
  "expiration": "2040-09-21T11:00:00.000Z",
  "storefronts": [
      {
          "name": "CurrencyStorefront",
          "catalogEntries": [
              {
                "devName": "[VIRTUAL]1 x Isabelle for 1200 MtxCurrency",
                "offerId": "v2:/f3d84c3ded015ae12a0c8ae3cc60d771a45df0d90f0af5e1cfbd454fa3083c94",
                "fulfillmentIds": [],
                "dailyLimit": -1,
                "weeklyLimit": -1,
                "monthlyLimit": -1,
                "categories": [
                    "Panel 03"
                ],
                "prices": [
                    {
                        "currencyType": "MtxCurrency",
                        "currencySubType": "",
                        "regularPrice": 1200,
                        "dynamicRegularPrice": 1200,
                        "finalPrice": 1200,
                        "saleExpiration": "9999-12-31T23:59:59.999Z",
                        "basePrice": 1200
                    }
                ],
                "meta": {
                    "NewDisplayAssetPath": "/Game/Catalog/NewDisplayAssets/DAv2_CID_A_042_F_Scholar.DAv2_CID_A_042_F_Scholar",
                    "offertag": "",
                    "SectionId": "Featured",
                    "TileSize": "Normal",
                    "AnalyticOfferGroupId": "3",
                    "ViolatorTag": "",
                    "ViolatorIntensity": "High",
                    "FirstSeen": ""
                },
                "matchFilter": "",
                "filterWeight": 0.0,
                "appStoreId": [],
                "requirements": [
                    {
                        "requirementType": "DenyOnItemOwnership",
                        "requiredId": "AthenaCharacter:CID_A_042_Athena_Commando_F_Scholar",
                        "minQuantity": 1
                    }
                ],
                "offerType": "StaticPrice",
                "giftInfo": {
                    "bIsEnabled": true,
                    "forcedGiftBoxTemplateId": "",
                    "purchaseRequirements": [],
                    "giftRecordIds": []
                },
                "refundable": true,
                "metaInfo": [
                    {
                        "key": "NewDisplayAssetPath",
                        "value": "/Game/Catalog/NewDisplayAssets/DAv2_CID_A_042_F_Scholar.DAv2_CID_A_042_F_Scholar"
                    },
                    {
                        "key": "offertag",
                        "value": ""
                    },
                    {
                        "key": "SectionId",
                        "value": "Featured"
                    },
                    {
                        "key": "TileSize",
                        "value": "Normal"
                    },
                    {
                        "key": "AnalyticOfferGroupId",
                        "value": "3"
                    },
                    {
                        "key": "ViolatorTag",
                        "value": ""
                    },
                    {
                        "key": "ViolatorIntensity",
                        "value": "High"
                    },
                    {
                        "key": "FirstSeen",
                        "value": ""
                    }
                ],
                "displayAssetPath": "/Game/Catalog/DisplayAssets/DA_Featured_CID_A_042_F_Scholar.DA_Featured_CID_A_042_F_Scholar",
                "itemGrants": [
                    {
                        "templateId": "AthenaCharacter:CID_A_042_Athena_Commando_F_Scholar",
                        "quantity": 1
                    }
                ],
                "additionalGrants": [],
                "sortPriority": -2,
                "catalogGroupPriority": 0
            }
          
          ]
      }
  ]
}
```
^ Generates Isabelle skin, using the 'Generate single item' command.

*Note: Your file will save as shop.json*

### How to install
- This program is made in [Python](https://www.python.org/), download the language to use this.
