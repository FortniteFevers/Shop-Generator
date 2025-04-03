# Shop-Generator
A program to generate custom Fortnite Item Shops - Specifically made for [Neonite](https://github.com/FortniteFevers/Shop-Generator/releases).
This program is inspired by the Shop Generator by [InTheShade](https://github.com/FortniteFevers/Shop-Generator/releases)

## 🚫 *CURRENTLY OUTDATED WITH THE LATEST FORTNITE VERSION*
## ❓ *WORKING ON A NEW VERSION ATM*

# Requirements
- [requests](https://github.com/FortniteFevers/Shop-Generator/releases)
- [pycryptodome](https://github.com/FortniteFevers/Shop-Generator/releases)

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
                    "NewDisplayAssetPath": "https://github.com/FortniteFevers/Shop-Generator/releases",
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
                        "value": "https://github.com/FortniteFevers/Shop-Generator/releases"
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
                "displayAssetPath": "https://github.com/FortniteFevers/Shop-Generator/releases",
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

*Note: Your file will save as https://github.com/FortniteFevers/Shop-Generator/releases*

### How to install
- This program is made in [Python](https://github.com/FortniteFevers/Shop-Generator/releases), download the language to use this.
