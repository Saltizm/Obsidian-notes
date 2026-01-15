---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Mapper ^COojd6A4

key, value, context ^BHT4ZL88

unique id ^RvBVEiAg

data fields ^uLi7iN1Y

formatted ^dCPYe380

.write(key, value)
    text -> string
    intwritable -> int ^m0SR3n1b

.toString().trim() ^YTyNaOA9

reducer ^8CqvMXdJ

key, value, context ^997qCXKQ

combine into output ^tAdDY95b

cumilate
and format ^CTMYwCBL

Runner ^uCjDr4cP

Init:
- job <- (configuration, "title")
- job.setJarbyClass(runner.class)
- job.setMapperClass(mapper.class)
- job.setReducerClass(reducer.class)

- job.setOutputKeyClass(keytype.class)    usually Text
- job.setOutputValueClass(keytype.class)  usually IntWritable

- job.setOutputFormatClass (not sure yet)

- FileInputFormat.addInputPath <- (job, new Path('path/to/input'))
- success = job.watiForCompletion(true);
- if success: System.exit(1)
- if not success: System.exit(0); ^fIt3Duda

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.23",
	"elements": [
		{
			"id": "j_20K8ISDJ_jd3cRrej_G",
			"type": "rectangle",
			"x": -243,
			"y": -169.0234375,
			"width": 294,
			"height": 359,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 1655222030,
			"version": 68,
			"versionNonce": 1257093714,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "bRKIo5KvSdq7l-1PbgRN1",
					"type": "arrow"
				}
			],
			"updated": 1760801973338,
			"link": null,
			"locked": false
		},
		{
			"id": "COojd6A4",
			"type": "text",
			"x": -230,
			"y": -207.0234375,
			"width": 67.91993713378906,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 268993486,
			"version": 26,
			"versionNonce": 1275487374,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760800673999,
			"link": null,
			"locked": false,
			"text": "Mapper",
			"rawText": "Mapper",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": "Mapper",
			"lineHeight": 1.25
		},
		{
			"id": "BHT4ZL88",
			"type": "text",
			"x": -215,
			"y": -140.0234375,
			"width": 186.93984985351562,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 957249166,
			"version": 30,
			"versionNonce": 1621689170,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "rJQV7DBQJtsJuO20r0kvM",
					"type": "arrow"
				},
				{
					"id": "YrFRKNO60GBQOL76GRZri",
					"type": "arrow"
				},
				{
					"id": "LqLvXGa_P-Y5oopKa8J4J",
					"type": "arrow"
				},
				{
					"id": "hvn2X7X2k7qVm4OVuB6yn",
					"type": "arrow"
				}
			],
			"updated": 1760800989980,
			"link": null,
			"locked": false,
			"text": "key, value, context",
			"rawText": "key, value, context",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": "key, value, context",
			"lineHeight": 1.25
		},
		{
			"id": "rJQV7DBQJtsJuO20r0kvM",
			"type": "arrow",
			"x": -209,
			"y": -113.0234375,
			"width": 96,
			"height": 47,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1443952014,
			"version": 22,
			"versionNonce": 1920652626,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760800731015,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-96,
					47
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "BHT4ZL88",
				"focus": 0.48615133797500176,
				"gap": 2
			},
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "RvBVEiAg",
			"type": "text",
			"x": -371,
			"y": -61.0234375,
			"width": 84.05992126464844,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1418083986,
			"version": 18,
			"versionNonce": 1460350414,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760800736957,
			"link": null,
			"locked": false,
			"text": "unique id",
			"rawText": "unique id",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": "unique id",
			"lineHeight": 1.25
		},
		{
			"id": "YrFRKNO60GBQOL76GRZri",
			"type": "arrow",
			"x": -158,
			"y": -112.0234375,
			"width": 1,
			"height": 57,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1492685390,
			"version": 162,
			"versionNonce": 350954898,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760800759884,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1,
					57
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "BHT4ZL88",
				"focus": 0.386362421167677,
				"gap": 3
			},
			"endBinding": {
				"elementId": "uLi7iN1Y",
				"focus": -0.02487694970858125,
				"gap": 13
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "uLi7iN1Y",
			"type": "text",
			"x": -214,
			"y": -42.0234375,
			"width": 111.89990234375,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 502488338,
			"version": 66,
			"versionNonce": 890445710,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "YrFRKNO60GBQOL76GRZri",
					"type": "arrow"
				},
				{
					"id": "6rlwZ49U09IseIp8FdiJw",
					"type": "arrow"
				}
			],
			"updated": 1760800765635,
			"link": null,
			"locked": false,
			"text": "data fields",
			"rawText": "data fields",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": "data fields",
			"lineHeight": 1.25
		},
		{
			"id": "6rlwZ49U09IseIp8FdiJw",
			"type": "arrow",
			"x": -142,
			"y": -4.0234375,
			"width": 81,
			"height": 47,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 742225618,
			"version": 211,
			"versionNonce": 248234830,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "dCPYe380"
				}
			],
			"updated": 1760800786821,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					46,
					37
				],
				[
					81,
					-10
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "uLi7iN1Y",
				"focus": 0.21894735229327503,
				"gap": 13
			},
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "dCPYe380",
			"type": "text",
			"x": -133.15995025634766,
			"y": 18.4765625,
			"width": 100.31990051269531,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 276848402,
			"version": 14,
			"versionNonce": 1480082062,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760800771477,
			"link": null,
			"locked": false,
			"text": "formatted",
			"rawText": "formatted",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 18,
			"containerId": "6rlwZ49U09IseIp8FdiJw",
			"originalText": "formatted",
			"lineHeight": 1.25
		},
		{
			"id": "LqLvXGa_P-Y5oopKa8J4J",
			"type": "arrow",
			"x": -62,
			"y": -16.0234375,
			"width": 10,
			"height": 87,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 2092665362,
			"version": 72,
			"versionNonce": 2010514830,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760800780708,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					10,
					-87
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "BHT4ZL88",
				"focus": -0.7622871941073891,
				"gap": 12
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "m0SR3n1b",
			"type": "text",
			"x": -31,
			"y": -54.0234375,
			"width": 204.11985778808594,
			"height": 75,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 201974802,
			"version": 97,
			"versionNonce": 364107662,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801174272,
			"link": null,
			"locked": false,
			"text": ".write(key, value)\n    text -> string\n    intwritable -> int",
			"rawText": ".write(key, value)\n    text -> string\n    intwritable -> int",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 68,
			"containerId": null,
			"originalText": ".write(key, value)\n    text -> string\n    intwritable -> int",
			"lineHeight": 1.25
		},
		{
			"id": "YTyNaOA9",
			"type": "text",
			"x": -173,
			"y": 65.9765625,
			"width": 156.1998291015625,
			"height": 25,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1176167890,
			"version": 38,
			"versionNonce": 1844142482,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760800888748,
			"link": null,
			"locked": false,
			"text": ".toString().trim()",
			"rawText": ".toString().trim()",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": ".toString().trim()",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 196,
			"versionNonce": 414305426,
			"isDeleted": false,
			"id": "gWRpoah-Q0IyXTw7N40uT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 293,
			"y": -179.5234375,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 294,
			"height": 359,
			"seed": 45350866,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "hvn2X7X2k7qVm4OVuB6yn",
					"type": "arrow"
				},
				{
					"id": "LpnhNXLGckFQSsWFx1f7m",
					"type": "arrow"
				}
			],
			"updated": 1760801027250,
			"link": null,
			"locked": false
		},
		{
			"id": "hvn2X7X2k7qVm4OVuB6yn",
			"type": "arrow",
			"x": -20,
			"y": -128.0234375,
			"width": 313,
			"height": 1,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 656358990,
			"version": 306,
			"versionNonce": 169331086,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801024320,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					313,
					-1
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "BHT4ZL88",
				"focus": -0.01372200140213555,
				"gap": 8.060150146484375
			},
			"endBinding": {
				"elementId": "gWRpoah-Q0IyXTw7N40uT",
				"focus": 0.7193971294414216,
				"gap": 1
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "8CqvMXdJ",
			"type": "text",
			"x": 300.0526315789474,
			"y": -213.44449013157896,
			"width": 71.85992431640625,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 743353614,
			"version": 171,
			"versionNonce": 2125625422,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "kilrSge5GjI4YAlKzrlSh",
					"type": "arrow"
				}
			],
			"updated": 1760801975651,
			"link": null,
			"locked": false,
			"text": "reducer",
			"rawText": "reducer",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": "reducer",
			"lineHeight": 1.25
		},
		{
			"id": "997qCXKQ",
			"type": "text",
			"x": 324,
			"y": -149.0234375,
			"width": 186.93984985351562,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 698020946,
			"version": 41,
			"versionNonce": 1465930318,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "lwZGtMR466Vfo4EBE8-NM",
					"type": "arrow"
				},
				{
					"id": "p6JPkpbPvRcYiW0okzwOQ",
					"type": "arrow"
				}
			],
			"updated": 1760801210911,
			"link": null,
			"locked": false,
			"text": "key, value, context",
			"rawText": "key, value, context",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": "key, value, context",
			"lineHeight": 1.25
		},
		{
			"id": "LpnhNXLGckFQSsWFx1f7m",
			"type": "arrow",
			"x": 293,
			"y": -130.0234375,
			"width": 104,
			"height": 39,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1875077070,
			"version": 105,
			"versionNonce": 1152034830,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801028910,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					62,
					-39
				],
				[
					104,
					-14
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "gWRpoah-Q0IyXTw7N40uT",
				"focus": -0.8179931206262604,
				"gap": 1
			},
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "lwZGtMR466Vfo4EBE8-NM",
			"type": "arrow",
			"x": 470,
			"y": 9.976562499999993,
			"width": 37,
			"height": 130,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 894553102,
			"version": 329,
			"versionNonce": 1098157074,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "tAdDY95b"
				}
			],
			"updated": 1760801205831,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					37,
					-71
				],
				[
					17,
					-130
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "997qCXKQ",
				"focus": -0.6543719008079615,
				"gap": 4
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "tAdDY95b",
			"type": "text",
			"x": 346.5200958251953,
			"y": -95.5234375,
			"width": 190.95980834960938,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 5141522,
			"version": 20,
			"versionNonce": 1947384590,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801193568,
			"link": null,
			"locked": false,
			"text": "combine into output",
			"rawText": "combine into output",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 18,
			"containerId": "lwZGtMR466Vfo4EBE8-NM",
			"originalText": "combine into output",
			"lineHeight": 1.25
		},
		{
			"id": "p6JPkpbPvRcYiW0okzwOQ",
			"type": "arrow",
			"x": 373,
			"y": -120.0234375,
			"width": 32,
			"height": 135,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 2129476050,
			"version": 167,
			"versionNonce": 1164984590,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "CTMYwCBL"
				}
			],
			"updated": 1760801251649,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-12,
					70
				],
				[
					20,
					135
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "997qCXKQ",
				"focus": 0.4355207807661911,
				"gap": 4
			},
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "CTMYwCBL",
			"type": "text",
			"x": 305.6200408935547,
			"y": -75.0234375,
			"width": 110.75991821289062,
			"height": 50,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1671950866,
			"version": 35,
			"versionNonce": 1891027662,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801250575,
			"link": null,
			"locked": false,
			"text": "cumilate\nand format",
			"rawText": "cumilate\nand format",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 43,
			"containerId": "p6JPkpbPvRcYiW0okzwOQ",
			"originalText": "cumilate\nand format",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 415,
			"versionNonce": 468095950,
			"isDeleted": false,
			"id": "MAP-zieiSW4M5NyY45rny",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -18.8947368421056,
			"y": -726.470805921052,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 703.4736842105265,
			"height": 423.2105263157895,
			"seed": 2083759570,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "bRKIo5KvSdq7l-1PbgRN1",
					"type": "arrow"
				},
				{
					"id": "kilrSge5GjI4YAlKzrlSh",
					"type": "arrow"
				}
			],
			"updated": 1760801975651,
			"link": null,
			"locked": false
		},
		{
			"id": "uCjDr4cP",
			"type": "text",
			"x": 283.8947368421049,
			"y": -768.0234374999994,
			"width": 63.13995361328125,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1770716690,
			"version": 117,
			"versionNonce": 2060215630,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801967071,
			"link": null,
			"locked": false,
			"text": "Runner",
			"rawText": "Runner",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": "Runner",
			"lineHeight": 1.25
		},
		{
			"id": "fIt3Duda",
			"type": "text",
			"x": 0.7368421052626672,
			"y": -716.4444901315785,
			"width": 660.7994384765625,
			"height": 375,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1477759246,
			"version": 828,
			"versionNonce": 2081429650,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801953271,
			"link": null,
			"locked": false,
			"text": "Init:\n- job <- (configuration, \"title\")\n- job.setJarbyClass(runner.class)\n- job.setMapperClass(mapper.class)\n- job.setReducerClass(reducer.class)\n\n- job.setOutputKeyClass(keytype.class)    usually Text\n- job.setOutputValueClass(keytype.class)  usually IntWritable\n\n- job.setOutputFormatClass (not sure yet)\n\n- FileInputFormat.addInputPath <- (job, new Path('path/to/input'))\n- success = job.watiForCompletion(true);\n- if success: System.exit(1)\n- if not success: System.exit(0);",
			"rawText": "Init:\n- job <- (configuration, \"title\")\n- job.setJarbyClass(runner.class)\n- job.setMapperClass(mapper.class)\n- job.setReducerClass(reducer.class)\n\n- job.setOutputKeyClass(keytype.class)    usually Text\n- job.setOutputValueClass(keytype.class)  usually IntWritable\n\n- job.setOutputFormatClass (not sure yet)\n\n- FileInputFormat.addInputPath <- (job, new Path('path/to/input'))\n- success = job.watiForCompletion(true);\n- if success: System.exit(1)\n- if not success: System.exit(0);",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 368,
			"containerId": null,
			"originalText": "Init:\n- job <- (configuration, \"title\")\n- job.setJarbyClass(runner.class)\n- job.setMapperClass(mapper.class)\n- job.setReducerClass(reducer.class)\n\n- job.setOutputKeyClass(keytype.class)    usually Text\n- job.setOutputValueClass(keytype.class)  usually IntWritable\n\n- job.setOutputFormatClass (not sure yet)\n\n- FileInputFormat.addInputPath <- (job, new Path('path/to/input'))\n- success = job.watiForCompletion(true);\n- if success: System.exit(1)\n- if not success: System.exit(0);",
			"lineHeight": 1.25
		},
		{
			"id": "bRKIo5KvSdq7l-1PbgRN1",
			"type": "arrow",
			"x": 79.68421052631612,
			"y": -281.7076480263152,
			"width": 116.84210526315792,
			"height": 85.26315789473688,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1081207246,
			"version": 71,
			"versionNonce": 2140871826,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801973338,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-116.84210526315792,
					85.26315789473688
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "MAP-zieiSW4M5NyY45rny",
				"focus": -0.10340234417124038,
				"gap": 21.552631578947285
			},
			"endBinding": {
				"elementId": "j_20K8ISDJ_jd3cRrej_G",
				"focus": -0.57182433488178,
				"gap": 27.421052631578334
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "kilrSge5GjI4YAlKzrlSh",
			"type": "arrow",
			"x": 337.5789473684213,
			"y": -282.76027960526255,
			"width": 5.263157894736878,
			"height": 61.05263157894734,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1436983314,
			"version": 33,
			"versionNonce": 1774119438,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1760801975651,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					5.263157894736878,
					61.05263157894734
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "MAP-zieiSW4M5NyY45rny",
				"focus": 0.04127868261402101,
				"gap": 20.499999999999943
			},
			"endBinding": {
				"elementId": "8CqvMXdJ",
				"focus": 0.23372093837167746,
				"gap": 8.263157894736253
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "4qopWnUf",
			"type": "text",
			"x": 437,
			"y": -95.5234375,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1496992146,
			"version": 2,
			"versionNonce": 109196110,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1760801188904,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 18,
			"containerId": "lwZGtMR466Vfo4EBE8-NM",
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "e9vSLKvQ",
			"type": "text",
			"x": 197.31578947368388,
			"y": -445.7865953947362,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1725447378,
			"version": 2,
			"versionNonce": 102419470,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1760801730849,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 18,
			"containerId": "MAP-zieiSW4M5NyY45rny",
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "sxhMqWVO",
			"type": "text",
			"x": 143.1052631578944,
			"y": -445.7865953947362,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 745006734,
			"version": 2,
			"versionNonce": 677313170,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1760801593273,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 18,
			"containerId": "MAP-zieiSW4M5NyY45rny",
			"originalText": "",
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 325.57894736842076,
		"scrollY": 594.2898848684205,
		"zoom": {
			"value": 0.95
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%