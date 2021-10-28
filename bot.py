import requests
import json
import time

with open(f'shop.json', 'w') as x:
    with open('empty.json') as f:
        ting = json.load(f)
    json.dump(ting, x, indent = 4)

a_file = open(f"shop.json", "r")
json_object = json.load(a_file)
a_file.close()

print('Welcome to Fevers Item Shop Generator bot - Inspired by InTheShade.')
print('\nWould you like to..')
print('(1) Generate single item')
print('(2) Generate Custom Set')
print('(3) Generate new cosmetics')
print('(4) Generate existing item set')
print('(5) Generate existing Item Bundle')

print('(C) Create an empty Fortnite Raw Shop')

ask = input('>> ')

if ask == '1':
    print('\nPlease enter the Item name.')
    id = input('>> ')

    response = requests.get(f'https://benbot.app/api/v1/cosmetics/br/search?lang=en&searchLang=en&matchMethod=full&name={id}')
    id = response.json()['id']
    name = response.json()['name']
    backendtype = response.json()['backendType']

    print('\nPlease enter a section ID for the item.')
    section = input('>> ')

    print('\nPlease enter a price for the item. (Enter number)')
    price = int(input('>> '))

    print('\nPlease enter a Tile Size for the item. (Small (1), Normal (2), DoubleWide (3)..)')
    tilesize = input('>> ')
    if tilesize == '1':
        tilesize = 'Small'
    elif tilesize == '2':
        tilesize = 'Normal'
    elif tilesize == '3':
        tilesize = 'DoubleWide'

    json_object['devName'] = f'[VIRTUAL]1 x {name} for {price} MtxCurrency'

    json_object['prices'] = [{
        "currencyType": "MtxCurrency",
        "currencySubType": "",
        "regularPrice": price,
        "dynamicRegularPrice": price,
        "finalPrice": price,
        "saleExpiration": "9999-12-31T23:59:59.999Z",
        "basePrice": price 
    }]

    json_object['requirements'] = [
        {
            "requirementType": "DenyOnItemOwnership",
            "requiredId": f"{backendtype}:{id}",
            "minQuantity": 1
        }
    ]

    da_id = id.replace('Athena_Commando_', '')

    json_object['meta']['NewDisplayAssetPath'] = f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}"
    
    json_object['meta']['SectionId'] = section

    json_object['meta']['TileSize'] = tilesize

    json_object['metaInfo'] = [
        {
            "key": "NewDisplayAssetPath",
            "value": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}"
        },
        {
            "key": "offertag",
            "value": ""
        },
        {
            "key": "SectionId",
            "value": f"{section}"
        },
        {
            "key": "TileSize",
            "value": f"{tilesize}"
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
    ]

    json_object['itemGrants'] = [
        {
            "templateId": f"{backendtype}:{id}",
            "quantity": 1
        }
    ]

    json_object['displayAssetPath'] = f'/Game/Catalog/DisplayAssets/DA_Featured_{da_id}.DA_Featured_{da_id}'
    print('Done!')

elif ask == '2': # 
    print('\nHow much items are in this custom set?')
    items = int(input('>> '))
    print('\nWhat Shop Section ID will this custom set be in?')
    section = input('>> ')
    print('\nDo you want to use a custom price for each item, or just use one stable price?\n(1): Multiple prices\n(2): Same price for each')
    customprice = input('>> ')
    if customprice == '1':
        customprice = True
    else:
        customprice = False
    
    count = []
    with open(f'shop.json', 'w') as x:
        json.dump(count, x, indent = 4)

    a_file = open(f"shop.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    for i in range(items):
        #print(str(i))
        num = i + 1
        print(f'\nPlease enter Item #{num}s name. (If name does not exist, you will have to start over again.)')
        id = input('>> ')

        response = requests.get(f'https://benbot.app/api/v1/cosmetics/br/search?lang=en&searchLang=en&matchMethod=full&name={id}')
        id = response.json()['id']
        da_id = id.replace('Athena_Commando_', '')
        name = response.json()['name']
        backendtype = response.json()['backendType']
        if customprice == False:
            price = 1
        else:
            print('\nWhat price should this item be?')
            price = int(input('>> '))
        tilesize = 'Normal'

        json_object.append({
            "devName": f"[VIRTUAL]1 x {name} for {price} MtxCurrency",
            "offerId": "v2:/f3d84c3ded015ae12a0c8ae3cc60d771a45df0d90f0af5e1cfbd454fa3083c94",
            "fulfillmentIds": [],
            "dailyLimit": -1,
            "weeklyLimit": -1,
            "monthlyLimit": -1,
            "categories": [
                "Panel 17"
            ],
            "prices": [
                {
                    "currencyType": "MtxCurrency",
                    "currencySubType": "",
                    "regularPrice": price,
                    "dynamicRegularPrice": price,
                    "finalPrice": price,
                    "saleExpiration": "9999-12-31T23:59:59.999Z",
                    "basePrice": price
                }
            ],
            "meta": {
                "NewDisplayAssetPath": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}",
                "offertag": "",
                "SectionId": f"{section}",
                "TileSize": f"{tilesize}",
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
                    "requiredId": f"{backendtype}:{id}",
                    "minQuantity": 1
                }
            ],
            "offerType": "StaticPrice",
            "giftInfo": {
                "bIsEnabled": True,
                "forcedGiftBoxTemplateId": "",
                "purchaseRequirements": [],
                "giftRecordIds": []
            },
            "refundable": True,
            "metaInfo": [
                {
                    "key": "NewDisplayAssetPath",
                    "value": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}"
                },
                {
                    "key": "offertag",
                    "value": ""
                },
                {
                    "key": "SectionId",
                    "value": f"{section}"
                },
                {
                    "key": "TileSize",
                    "value": f"{tilesize}"
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
            "displayAssetPath": f"/Game/Catalog/DisplayAssets/DA_Featured_{da_id}.DA_Featured_{da_id}",
            "itemGrants": [
                {
                    "templateId": f"{backendtype}:{id}",
                    "quantity": 1
                }
            ],
            "additionalGrants": [],
            "sortPriority": -2,
            "catalogGroupPriority": 0
        })

elif ask == '3':
    response = requests.get(f'https://benbot.app/api/v1/newCosmetics')

    print('\nPlease enter a section ID for new items.')
    section = input('>> ')

    print('\nDo you only want to get new skins?\n(1): Yes\n(2): No, generate all new cosmetics')
    onlyskins = input('>> ')
    if onlyskins == '1':
        onlyskins = True
    else:
        onlyskins = False

    count = []
    with open(f'shop.json', 'w') as x:
        json.dump(count, x, indent = 4)

    a_file = open(f"shop.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    for i in response.json()['items']:
        start = time.time()
        price = 000
        tilesize = 'Normal'
        id = i['id']
        backendtype = i['backendType']
        name = i['name']
        da_id = id.replace('Athena_Commando_', '')
        #r = requests.get(f'https://benbot.app/api/v1/files/search?path=/Game/Catalog/NewDisplayAssets/DAv2_{da_id}')
        #try:
        #    load = json.loads(r)
        #except:
        #    tilesize = 'Small'
        if onlyskins == True:
            if backendtype == 'AthenaCharacter':
                json_object.append({
                    "devName": f"[VIRTUAL]1 x {name} for {price} MtxCurrency",
                    "offerId": "v2:/f3d84c3ded015ae12a0c8ae3cc60d771a45df0d90f0af5e1cfbd454fa3083c94",
                    "fulfillmentIds": [],
                    "dailyLimit": -1,
                    "weeklyLimit": -1,
                    "monthlyLimit": -1,
                    "categories": [
                        "Panel 17"
                    ],
                    "prices": [
                        {
                            "currencyType": "MtxCurrency",
                            "currencySubType": "",
                            "regularPrice": price,
                            "dynamicRegularPrice": price,
                            "finalPrice": price,
                            "saleExpiration": "9999-12-31T23:59:59.999Z",
                            "basePrice": price
                        }
                    ],
                    "meta": {},
                    "matchFilter": "",
                    "filterWeight": 0.0,
                    "appStoreId": [],
                    "requirements": [
                        {
                            "requirementType": "DenyOnItemOwnership",
                            "requiredId": f"{backendtype}:{id}",
                            "minQuantity": 1
                        }
                    ],
                    "offerType": "StaticPrice",
                    "giftInfo": {
                        "bIsEnabled": True,
                        "forcedGiftBoxTemplateId": "",
                        "purchaseRequirements": [],
                        "giftRecordIds": []
                    },
                    "refundable": True,
                    "metaInfo": [
                        {
                            "key": "NewDisplayAssetPath",
                            "value": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}"
                        },
                        {
                            "key": "SectionId",
                            "value": f"{section}"
                        },
                        {
                            "key": "TileSize",
                            "value": f"{tilesize}"
                        },
                        {
                            "key": "AnalyticOfferGroupId",
                            "value": "3"
                        }
                    ],
                    "displayAssetPath": f"/Game/Catalog/DisplayAssets/DA_Featured_{da_id}.DA_Featured_{da_id}",
                    "itemGrants": [
                        {
                            "templateId": f"{backendtype}:{id}",
                            "quantity": 1
                        }
                    ],
                    "additionalGrants": [],
                    "sortPriority": -2,
                    "catalogGroupPriority": 0
                })
        else:
            json_object.append({
                "devName": f"[VIRTUAL]1 x {name} for {price} MtxCurrency",
                    "offerId": "v2:/f3d84c3ded015ae12a0c8ae3cc60d771a45df0d90f0af5e1cfbd454fa3083c94",
                    "fulfillmentIds": [],
                    "dailyLimit": -1,
                    "weeklyLimit": -1,
                    "monthlyLimit": -1,
                    "categories": [
                        "Panel 17"
                    ],
                    "prices": [
                        {
                            "currencyType": "MtxCurrency",
                            "currencySubType": "",
                            "regularPrice": price,
                            "dynamicRegularPrice": price,
                            "finalPrice": price,
                            "saleExpiration": "9999-12-31T23:59:59.999Z",
                            "basePrice": price
                        }
                    ],
                    "meta": {
                        "NewDisplayAssetPath": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}",
                        "SectionId": f"{section}",
                        "TileSize": f"{tilesize}",
                        "AnalyticOfferGroupId": ""
                    },
                    "matchFilter": "",
                    "filterWeight": 0.0,
                    "appStoreId": [],
                    "requirements": [
                        {
                            "requirementType": "DenyOnItemOwnership",
                            "requiredId": f"{backendtype}:{id}",
                            "minQuantity": 1
                        }
                    ],
                    "offerType": "StaticPrice",
                    "giftInfo": {
                        "bIsEnabled": True,
                        "forcedGiftBoxTemplateId": "",
                        "purchaseRequirements": [],
                        "giftRecordIds": []
                    },
                    "refundable": True,
                    "metaInfo": [
                        {
                            "key": "NewDisplayAssetPath",
                            "value": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}"
                        },
                        {
                            "key": "SectionId",
                            "value": f"{section}"
                        },
                        {
                            "key": "TileSize",
                            "value": f"{tilesize}"
                        },
                        {
                            "key": "AnalyticOfferGroupId",
                            "value": ""
                        }
                    ],
                    "displayAssetPath": f"/Game/Catalog/DisplayAssets/DA_Featured_{da_id}.DA_Featured_{da_id}",
                    "itemGrants": [
                        {
                            "templateId": f"{backendtype}:{id}",
                            "quantity": 1
                        }
                    ],
                    "additionalGrants": [],
                    "sortPriority": -2,
                    "catalogGroupPriority": 0
                })
    end = time.time()

    print(f'Finished in {end - start} seconds lmao')

elif ask == '4':
    print('What existing Item Set do you want to generate?')
    set = input('>> ')
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?set={set}')

    print('\nPlease enter a section ID for new items.')
    section = input('>> ')

    print('Please enter a price for every item.')
    price = int(input('>> '))

    count = []
    with open(f'shop.json', 'w') as x:
        json.dump(count, x, indent = 4)

    a_file = open(f"shop.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    start = time.time()
    for i in response.json()['data']:
        tilesize = 'Normal'
        id = i['id']
        backendtype = i['type']['backendValue']
        name = i['name']
        da_id = id.replace('Athena_Commando_', '')
        json_object.append({
            "devName": f"[VIRTUAL]1 x {name} for {price} MtxCurrency",
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
                    "regularPrice": price,
                    "dynamicRegularPrice": price,
                    "finalPrice": price,
                    "saleExpiration": "9999-12-31T23:59:59.999Z",
                    "basePrice": price
                }
            ],
            "meta": {
                "NewDisplayAssetPath": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}",
                "offertag": "",
                "SectionId": f"{section}",
                "TileSize": f"{tilesize}",
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
                    "requiredId": f"{backendtype}:{id}",
                    "minQuantity": 1
                }
            ],
            "offerType": "StaticPrice",
            "giftInfo": {
                "bIsEnabled": True,
                "forcedGiftBoxTemplateId": "",
                "purchaseRequirements": [],
                "giftRecordIds": []
            },
            "refundable": True,
            "metaInfo": [
                {
                    "key": "NewDisplayAssetPath",
                    "value": f"/Game/Catalog/NewDisplayAssets/DAv2_{da_id}.DAv2_{da_id}"
                },
                {
                    "key": "offertag",
                    "value": ""
                },
                {
                    "key": "SectionId",
                    "value": f"{section}"
                },
                {
                    "key": "TileSize",
                    "value": f"{tilesize}"
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
            "displayAssetPath": f"/Game/Catalog/DisplayAssets/DA_Featured_{da_id}.DA_Featured_{da_id}",
            "itemGrants": [
                {
                    "templateId": f"{backendtype}:{id}",
                    "quantity": 1
                }
            ],
            "additionalGrants": [],
            "sortPriority": -2,
            "catalogGroupPriority": 0
        })
    end = time.time()

    print(f'Finished in {end - start} seconds lmao')

elif ask == '5':
    print('Please note: This bundle will be automatically put into the LimitedTime section ID. (This is so that it appears in your shop without any bugs)')

    print('\nDo you want to generate a dynamic bundle or item bundle?\n(1): Dynamic\n(2): Normal')
    bundletype = input('>> ')

    print('\nPlease tell me the bundle name.')
    bundlename = input('>> ')

    print('\nPlease input the bundle price you want it to be. (Enter number)')
    price = int(input('>> '))

    print('\nPlease input the bundle NEW display asset file name.') # Example: DAv2_RMT_MagmaMasters
    newda = input('>> ')

    print('\nPlease input the NORMAL dispaly asset file name.') # Example: DA_Featured_MagmaLegendsBundle
    da = input('>> ')
    
    ting = []
    with open(f'shop.json', 'w') as x:
        json.dump(ting, x, indent = 4)

    a_file = open(f"shop.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    if bundletype == '1':
        json_object.append(
            {
                "offerId": "9C4C1DC4415C44FD20C854992634F57F",
                "devName": f"{bundlename}",
                "offerType": "StaticPrice",
                "fulfillmentIds": [],
                "prices": [
                    {
                        "currencyType": "MtxCurrency",
                        "currencySubType": "",
                        "regularPrice": price,
                        "dynamicRegularPrice": -1,
                        "finalPrice": price,
                        "saleExpiration": "9999-12-31T23:59:59.999Z",
                        "basePrice": price
                    }
                ],
                "meta": {
                    "NewDisplayAssetPath": f"/Game/Catalog/NewDisplayAssets/{newda}.{newda}",
                    "SectionId": "LimitedTime",
                    "TileSize": "DoubleWide",
                    "AnalyticOfferGroupId": "2"
                },
                "categories": [],
                "dailyLimit": -1,
                "weeklyLimit": -1,
                "monthlyLimit": -1,
                "refundable": False,
                "appStoreId": [],
                "requirements": [
                    {
                        "requirementType": "DenyOnFulfillment",
                        "requiredId": "71D843404DB23C14AEF21C88C62FCFDE",
                        "minQuantity": 1
                    }
                ],
                "metaInfo": [
                    {
                        "key": "SectionID",
                        "value": "LimitedTime"
                    },
                    {
                        "key": "NewDisplayAssetPath",
                        "value": f"/Game/Catalog/NewDisplayAssets/{newda}.{newda}"
                    },
                    {
                        "key": "TileSize",
                        "value": "DoubleWide"
                    },
                    {
                        "key": "AnalyticOfferGroupId",
                        "value": "2"
                    }
                ],
                "catalogGroup": "",
                "catalogGroupPriority": 0,
                "sortPriority": 12,
                "title": f"{bundlename}",
                "shortDescription": "",
                "description": "TBD",
                "displayAssetPath": f"/Game/Catalog/DisplayAssets/{da}.{da}",
                "itemGrants": []
            }
        )
    else:
        json_object.append(
            {
                "devName": f"{bundlename}",
                "offerId": "v2:/ab5b9186b4a65fd4543e697aea9e63a7c40e7e7b22ece8f70101c6800f72a7ad",
                "fulfillmentIds": [],
                "dailyLimit": -1,
                "weeklyLimit": -1,
                "monthlyLimit": -1,
                "categories": [
                    "Panel 03"
                ],
                "prices": [],
                "dynamicBundleInfo": {
                    "discountedBasePrice": price,
                    "regularBasePrice": 0,
                    "floorPrice": price,
                    "currencyType": "MtxCurrency",
                    "currencySubType": "",
                    "displayType": "AmountOff",
                    "bundleItems": []
                },
                "meta": {
                    "NewDisplayAssetPath": f"/Game/Catalog/NewDisplayAssets/{newda}.{newda}",
                    "SectionId": "LimitedTime",
                    "TileSize": "DoubleWide",
                    "AnalyticOfferGroupId": "3"
                },
                "matchFilter": "",
                "filterWeight": 0.0,
                "appStoreId": [],
                "requirements": [],
                "offerType": "DynamicBundle",
                "giftInfo": {
                    "bIsEnabled": True,
                    "forcedGiftBoxTemplateId": "",
                    "purchaseRequirements": [],
                    "giftRecordIds": []
                },
                "refundable": True,
                "metaInfo": [
                    {
                        "key": "NewDisplayAssetPath",
                        "value": f"/Game/Catalog/NewDisplayAssets/{newda}.{newda}"
                    },
                    {
                        "key": "SectionId",
                        "value": "LimitedTime"
                    },
                    {
                        "key": "TileSize",
                        "value": "DoubleWide"
                    },
                    {
                        "key": "AnalyticOfferGroupId",
                        "value": "3"
                    }
                ],
                "displayAssetPath": f"Game/Catalog/DisplayAssets/{da}.{da}",
                "itemGrants": [],
                "additionalGrants": [],
                "sortPriority": -1,
                "catalogGroupPriority": 0
            },
        )
    a_file = open(f"shop.json", "w")
    json.dump(json_object, a_file, indent = 4)
    print('\nHow much items are in this bundle? (Enter number)')
    itemnum = int(input('>> '))
    for i in range(itemnum):
        realnum = i + 1
        print(f'\nWhat will item name #{realnum} be?')
        ask = input('>> ')
        response = None
        while response is None:
            try:
                response = requests.get(f'https://benbot.app/api/v1/cosmetics/br/search?name={ask}')
                #if response.json()['error'] == 'Could not find any cosmetic matching parameters':
                #    print('\nCould not find item with matching parameters.')
                #    print(f'Please enter an item ID instead.')
                #    itemid = input('>> ')
                #    response = requests.get(f'https://benbot.app/api/v1/cosmetics/br/search?id={itemid}')
                test = response.json()['id']
            except:
                print('Write ID instead')
                ask = input('>> ')
                response = requests.get(f'https://benbot.app/api/v1/cosmetics/br/search?id={ask}')
        id = response.json()['id']
        backendtype = response.json()['backendType']

        json_object[0]['itemGrants'].append(
            {
                "templateId": f"{backendtype}:{id}",
                "quantity": 1
            }
        )

        if bundletype == '2':
            json_object[0]['requirements'].append(
                {
                    "bCanOwnMultiple": False,
                    "regularPrice": 0,
                    "discountedPrice": 0,
                    "alreadyOwnedPriceReduction": 0,
                    "item": {
                        "templateId": f"{backendtype}:{id}",
                        "quantity": 1
                    }
                }
            )

elif ask == 'c' or ask == 'C':
    with open(f'shopraw.json', 'w') as x:
        ting = {
            "refreshIntervalHrs": 1,
            "dailyPurchaseHrs": 24,
            "expiration": "2040-09-21T11:00:00.000Z",
            "storefronts": [
                {
                    "name": "BRStarterKits",
                    "catalogEntries": []
                },
                
                {
                    "name": "BRDailyStorefront",
                    "catalogEntries":[]
                }

            ]
        }

        json.dump(ting, x, indent = 4)

else:
    print(f'\n"{ask}" is not a correct response. Please re-run the program and try again.')
    exit()

a_file = open(f"shop.json", "w")
json.dump(json_object, a_file, indent = 4)
print('dumped json into file')

time.sleep(2)
