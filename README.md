<div align="center">
  <p>
    <a href="#"><img src="images\d.jpeg" width="600" height="300" alt="overview image" /></a>
  </p>
</div>


<h1 style="text-align:center;">  Alibaba-CLI-Scraper </h1>
<h2 style="text-align:center;"> 🛒 💻 🕸 </h2>


---
Is a python package that provides a dedicated CLI interface for scraping data from Alibaba.com.
The purpose of this project is to extract products and theirs related suppliers informations from Alibaba.com and store it in a local database (SQLite or MySQL). The project utilizes asynchronous requests for efficient handling of numerous requests and allows users to easily run the scraper and manage the database using a user-friendly command-line interface (CLI).

### Features:

* **Asynchronous API:** Utilizes asynchronous API of Playwright and Brightdata Proxies for efficient handling of numerous pages results.
* **Database Integration:**  Stores scraped data in a database (SQLite or MySQL) for structured persistence.
* **User-Friendly CLI:** Provides easy-to-use commands for running the scraper and managing the database.
  
### Sample of CSV output
 id	name	alibaba_guranteed	minimum_to_order	supplier_id	alibaba_guranteed	certifications	ordered_or_sold	product_score	review_count	review_score	shipping_time_score	is_full_promotion	is_customizable	is_instant_order	trade_product	min_price	max_price	name	verification_mode	sopi_level	country_name	years_as_gold_supplier	supplier_service_score

1	mesh knitting weaving machine produce sunscreen net agricultural shade net anti net	1	1	1	1		0	5.0	1.0	5.0	5.0	1	1	1	1	9997.0	18979.0	qingdao shanzhong imp and exp ltd.	unverified	0	chine	9	5.0

2	chinese small farm rotary tiller 12hp 15hp 20hp two wheel mini hand tractor walk behind tractors	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	455.0	455.0	shandong guoyoule agricultural machinery co., ltd.	unverified	0	chine	1	0.0

3	small multifunctional flexible 130l orchard remote control garden crawler agriculture robot sprayer	1	1	3	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2350.0	4620.0	shandong my agricultural facilities co., ltd.	unverified	0	chine	1	0.0

4	5hp/7hp/12hp rotary electric start agricultural farming walking tractor power tiller weeder cultivators	1	1	4	1		2	0.0	0.0	0.0	0.0	1	1	1	1	244.0	371.0	shandong jinlong lutai international trade co., ltd.	verified	0	chine	1	0.0

5	free shipping 3.5 ton mini excavator 1 ton 2 ton kubota engine digger excavator mini pelle chinese cheap small excavator machine	1	1	5	1	CE	95	4.6	25.0	4.6	4.6	1	1	1	1	988.0	1235.0	shandong qilu industrial co., ltd.	unverified	5	chine	4	4.6

6	olive harvester machine design battery pack used in olive harvest machines electric equipped with big capacity battery pack new	1	1	6	1	CE	0	4.3	6.0	4.6	4.6	1	1	1	1	260.0	260.0	zhejiang n plus intelligent technology co., ltd.	unverified	5	chine	7	5.0

7	hot sales 30l 2 4 stroke gasoline engine agriculture spray machine knapsack power sprayer	1	2	7	1	CE	2	5.0	1.0	5.0	5.0	1	1	1	1	40.8	55.87	taizhou yizhou agricultural machinery co., ltd.	unverified	0	chine	1	5.0

8	agriculture machinery combine harvester for rice and wheat	1	1	8	1		0	5.0	3.0	5.0	5.0	1	1	1	1	27800.0	29800.0	jiangsu minnuo group co., ltd.	unverified	5	chine	6	5.0

9	made in china agriculture machine seeder factory directly provide corn seed planter	1	1	9	1		26	5.0	5.0	5.0	5.0	1	1	1	1	2270.0	2280.0	liaocheng jade outdoor power equipment co., ltd	unverified	5	chine	4	5.0

10	agricultural machinery farm equipment mini rotary tiller 25hp 35hp	1	1	10	1		0	4.8	126.0	4.7	4.6	1	1	1	1	1000.0	2550.0	shandong hightop group	unverified	5	chine	9	4.7

11	latest agriculture machine hand held weeding machine / mini gasoline power weeder	1	1	11	1		2	4.6	14.0	4.6	4.5	1	1	1	1	35.0	200.0	henan best machinery co., ltd.	unverified	2	chine	10	4.7

12	2 stroke 52cc hand held garden tiller gasoline cultivator agriculture machine	1	2	12	1		0	4.7	22.0	4.8	4.9	1	1	1	1	89.0	100.0	shanghai yanto industry co., ltd.	unverified	3	chine	13	4.8

13	tractor mounted machines agricultural rotary grass cutter slasher	1	10	13	1		0	5.0	8.0	5.0	5.0	1	1	1	1	400.0	600.0	henan qianli machinery co., ltd.	unverified	3	chine	14	5.0

14	small agriculture machine one row corn picker mini walking tractor single row maize harvesting machine	1	1	14	1	CE	234	4.8	125.0	4.7	4.7	1	1	1	1	520.0	520.0	luohe xingdian electromechanical equipment co., ltd.	unverified	3	chine	4	4.7

15	second hand/new tractor 4x4wd new holland 4710 with loader and farming equipment agricultural machinery for sale	1	1	15	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	3500.0	akgok gmbh	unverified	2	autriche	2	0.0

16	diesel chain rail type small micro-tiller agricultural plowing and tilling machine small agricultural tillage machinery	1	1	16	1		9	4.5	30.0	4.5	4.5	1	1	1	1	242.0	242.0	dongguan city secondary idea cross border e-commerce co., ltd.	unverified	2	chine	1	4.5

17	2024 hot selling heavy duty harrow plough agriculture machinery disc harro for sale farm machinery	1	5	17	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5575.0	5575.0	jeegee agri. equip. manufacturing co., ltd.	unverified	0	chine	1	0.0

18	combined 4*4 50hp-80hp wheel farm tractor agricultural machinery	1	1	18	1	CE	2	4.5	14.0	4.5	4.5	1	1	1	1	3800.0	4000.0	weifang shengxuan machinery co., ltd.	unverified	2	chine	16	4.5

19	china 70hp 80hp 90hp 100hp 4wd farm tractor price agricultural machinery	1	1	19	1	CE	0	4.8	9.0	4.7	4.6	1	1	1	1	5000.0	5000.0	shandong tavol group co.,ltd	unverified	3	chine	8	4.7

20	factory price agricultural machinery farming tools gasoline cultivator tiller	1	2	20	1	CE	1	4.9	42.0	4.9	4.9	1	1	1	1	76.0	85.0	shaoxing haotuo machinery co., ltd.	unverified	3	chine	6	4.9

21	agricultural machinery peeling husking grinder combine diesel rice mil machine 40 tpd	1	1	21	1		2	4.1	29.0	4.4	4.6	1	1	1	1	142.0	146.0	shuangfeng xiangdong machinery manufacturing co., ltd.	unverified	1	chine	6	4.5

22	quality strong running 4wd kubota tractor m9540 60hp 75hp 80hp 120hp farm tractor agricultural machinery available for sale	1	1	22	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	4800.0	t and t invest gmbh	unverified	2	allemagne	1	0.0

23	mini tractor 30hp 40hp 2wd 4wd 4x4 tractor traktor tractors for agriculture agricultural machinery for sale	1	1	10	1	CE	0	4.8	31.0	4.8	4.7	1	1	1	1	2000.0	3500.0	gongyi vansen machinery equipment co., ltd.	unverified	3	chine	5	4.6

24	vansen factory small scale machinery > agricultural machinery & equipment > feed processing machines	1	1	23	1	CE	29	4.7	11.0	4.6	4.6	1	1	1	1	880.0	950.0	taian hysoon machinery co., ltd.	unverified	2	chine	16	0.0

25	mini agriculture tiller, mini multipurpose agricultural machine	1	1	24	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7580.0	7580.0	s v machinery india	unverified	2	inde	5	0.0

26	factory sale quality new super farm agricultural machinery 4wd tractor for sale (all models available)	1	1	25	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8700.0	8900.0	drazle inc	unverified	2	canada	1	0.0

27	new massey ferguson 8s.245 tractor agricultural machinery & equipment	1	1	26	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	3500.0	talaythong factory co., ltd.	unverified	1	tha�lande	8	0.0

28	agricultural machinery /thailand power tiller / walking tractor /hot sale price	1	10	27	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	1200.0	qingzhou keda environment protection machinery co., ltd.	unverified	3	chine	11	5.0

29	keda agricultural machinery & equipment full automatic hydraulic seaweed harvesting machines	1	1	28	1		0	5.0	4.0	5.0	5.0	1	1	1	1	23800.0	23800.0	jining tiande engineering machinery co., ltd.	unverified	2	chine	6	5.0

30	agricultural machine harvesting natural grass alfalfa lawn mower grass cutting machine for sale	1	1	29	1		0	4.9	10.0	4.9	4.9	1	1	1	1	300.0	323.0	shanghai vostosun industrial co., ltd.	unverified	3	chine	7	5.0

31	mini massey ferguson 65 tractor eos implementer farm irrigation systems used agricultural machinery & equipment	1	1	30	1		0	5.0	3.0	5.0	5.0	1	1	1	1	35100.0	40000.0	active global trade inc.	unverified	2	canada	1	0.0

32	high efficiency original used massey ferguson mf 399 tractor agricultural machinery	1	1	31	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3100.0	3100.0	zhejiang shengshi yuanlin technology co., ltd.	unverified	3	chine	7	5.0

33	high quality orchard crop 20l sprayer agricultural machine for sale	1	1	32	1		21	5.0	1.0	5.0	5.0	1	1	1	1	20.9	22.1	hunan tingxiang mechanical and electrical technology co., ltd.	unverified	1	chine	1	5.0

34	tx agricultural machinery mini land cultivation machine 5hp 7hp garden tractor cultivators home power tiller cultivator diesel	1	1	33	1		2	4.8	8.0	4.9	5.0	1	1	1	1	105.0	110.0	zhengzhou use well machinery co., ltd.	unverified	2	chine	4	4.9

35	agricultural machinery small mobile ventilation seed grain paddy corn wheat rice drying dryer machine	1	1	34	1		0	4.9	12.0	4.8	4.8	1	1	1	1	1490.0	1520.0	weifang langpak international co., ltd.	unverified	0	chine	5	4.7

36	2wd 4x2 20hp agricultural machinery & equipment tractors agriculture for farm	1	1	35	1		8	4.5	7.0	4.5	4.5	1	1	1	1	1700.0	2200.0	rock co., ltd.	unverified	2	japon	1	0.0

37	japanese high quality product rice agricultural machinery used	1	1	36	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	15000.0	sarl coll'dis	unverified	2	france	3	0.0

38	massey ferguson 8s.245 tractor agricultural machinery / farm tractor available	1	1	37	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	3500.0	zhengzhou microcarr trading co., ltd.	unverified	2	chine	2	4.6

39	mini agriculture chaff cutters machines multifunctional provided poultry farm grass machine for farms animal 600kg/h	1	1	38	1		21	4.8	18.0	4.7	4.7	1	1	1	1	180.0	190.0	henan bolong import&export trading co., ltd.	unverified	3	chine	4	4.5

40	agriculture machinery equipment manufacturer cow pig chicken manure dehydrator machine	1	1	39	1		0	4.5	2.0	4.5	4.5	1	1	1	1	1718.0	1773.0	eurl jap	unverified	2	france	1	0.0

41	excellent condition case ih tractor agricultural machinery / 110hp case ih tractor available	1	1	40	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3600.0	3600.0	yancheng shunyu agricultural machinery co., ltd.	unverified	2	chine	10	5.0

42	agriculture machinery ploughing machine 3 point disc plough mounted with farm tractor	1	10	41	1		36	5.0	11.0	4.9	4.9	1	1	1	1	1800.0	2200.0	yantai grand industry co.ltd.	unverified	1	chine	4	5.0

43	gasoline tilling machine and agriculture machinery equipment mini tiller	1	1	42	1		0	5.0	2.0	5.0	5.0	1	1	1	1	320.0	385.0	henan quanheng machinery equipment co., ltd.	unverified	0	chine	1	0.0

44	cultivators mini agriculture products farming equipment two wheel walking tractor garden tiller farming machinery agricultural	1	1	43	1		0	0.0	0.0	0.0	0.0	1	1	1	1	140.0	150.0	tai zhou  jc  machinery technology co., ltd	unverified	2	chine	4	4.8

45	taizhou jc-188 factory direct sale tiller cultivators fuel efficient agricultural machinery weeder	1	1	44	1		30	4.4	7.0	4.7	4.8	1	1	1	1	348.0	388.0	henan baba trading co.,ltd.	unverified	1	chine	1	5.0

46	hot sale cheap 4/6 rows agriculture planting machine for rice and vegetable seeds	1	1	45	1		1	5.0	3.0	5.0	5.0	1	1	1	1	130.0	594.28	weifang huabo agricultural equipment co., ltd.	unverified	1	chine	6	0.0

47	100hp 110hp 4x4 farm traktor / tractor agricultural machinery for sale	1	1	46	1		0	0.0	0.0	0.0	0.0	1	1	1	1	10000.0	15000.0	qingdao flyer agricultural equipment co., ltd.	unverified	2	chine	4	4.3

48	multifunctional 30hp 4wd farm tractor agricultural machine with front end loader and backhoe for sale	1	1	47	1	CE	0	4.4	13.0	4.3	4.3	1	1	1	1	1999.0	2999.0	sarl stokel trade	unverified	2	france	1	0.0

49	masseyy furgusonn 390 agricultural machinery / used 85hp mf390 farm tractor available for sale	1	1	48	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0	chongqing fengjiutian agricultural machinery co., ltd.	unverified	0	chine	1	0.0

50	tp-qwr-qyj tianpo factory supply multi-function quinoa wheat millet rice thresher rice sheller agriculture machine for farm	1	1	49	1		0	0.0	0.0	0.0	0.0	1	1	1	1	139.0	148.0	shandong kaipeng agricultural machinery co., ltd.	unverified	0	chine	1	0.0

51	agricultural machinery feed baling machine square baler square silage balers machine	1	1	50	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1900.0	2155.0	fluid india	unverified	1	inde	1	0.0

52	direct factory supply fogging system 570 x 175 x 400 mm agricultural machinery & equipment jet fogger for sale	1	10	51	1		0	0.0	0.0	0.0	0.0	1	1	1	1	43.0	48.0	shunda mould technology co., ltd.	unverified	0	chine	1	0.0

53	good service high quality agricultural machinery pedestrian rice transplanter seeder high-speed plant machine	1	1	52	1		0	0.0	0.0	0.0	0.0	1	1	1	1	11800.0	11800.0	weifang diyuan machinery technology co., ltd.	unverified	0	chine	1	5.0

54	china mini/small/large/diesel/garden/agricultural machinery wheel farm tractor small tractor soil bed making machine	1	1	53	1		0	5.0	3.0	5.0	5.0	1	1	1	1	22800.0	22860.0	tai'an daiding machinery manufacturing co., ltd	unverified	1	chine	1	5.0

55	manufacture canopy orange tractor agricultural machinery with diesel engine for farm use	1	1	54	1		0	5.0	1.0	5.0	5.0	1	1	1	1	5950.0	5999.0	tractus llc	unverified	0	�tats-unis	1	0.0

56	ce approved mini round straw hay baler new farm agriculture machinery	1	1	55	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0	shijiazhuang zengfa machinery equipment sales co., ltd	unverified	0	chine	1	0.0

57	free shipping brand 40 horsepower four-wheel drive tractor agricultural machinery traction drive operation machinery	1	1	56	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9900.0	9900.0	qinyang xingta machinery co., ltd.	unverified	0	chine	1	0.0

58	farm tools machinery wheat planters matched tractors 6-9 rows wheat seeder agricultural machinery	1	1	57	1		0	0.0	0.0	0.0	0.0	1	1	1	1	680.0	680.0	automotive  llc	unverified	0	�tats-unis	1	0.0

59	used massey ferguson farm tractors farm tractor agriculture machinery for sale farm used tractor	1	1	58	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5500.0	5500.0	hebei shuoying machinery equipment co., ltd.	unverified	0	chine	1	0.0

60	25-60hp mini tractor agricultural machinery for farm use	1	1	59	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3900.0	4500.0	kosai shoten	unverified	0	japon	1	0.0

61	outstanding quality japanese spraying plowing tractor small agricultural machinery	1	2	60	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	100000.0	t.s. trading & exporting, llc.	unverified	1	�tats-unis	1	0.0

62	case ih 9350 tractor agricultural machinery & equipment	1	1	62	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	5000.0	automobile go llc	unverified	3	�tats-unis	1	0.0

63	multifunctional crawler agricultural machinery flood and drought mini rotary tiller cultivator machinery	1	1	63	1		0	4.4	4.0	4.3	4.0	1	1	1	1	3166.0	3166.0	hainan free trade zone baiya plastic products co., ltd.	unverified	1	chine	1	4.5

64	agricultural machinery intelligent irrigation system installed automatic water and fertilizer machine	1	1	64	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2700.0	2900.0	hubei wings of water technology co., ltd.	unverified	0	chine	1	0.0

65	portable garden small power tiller diesel engine micro cultivator 13hp seed drill cultivators mini agricultural machine	1	1	65	1		0	5.0	4.0	5.0	5.0	1	1	1	1	420.0	440.0	xiamen zexu import and export co., ltd.	unverified	0	chine	1	5.0

66	agricultural machinery corn silage harvester corn harvester tractor mounted machine	1	1	66	1		0	5.0	1.0	5.0	5.0	1	1	1	1	900.0	950.0	zhengzhou queb machinery co., ltd.	unverified	1	chine	1	5.0

67	agricultural machinery sensor controlled euro-jabelmann box tipper kkg 2250 fully automatic box tipping machine	1	1	67	1		0	0.0	0.0	0.0	0.0	1	1	1	1	18295.0	18295.0	euro-jabelmann maschinenbau gmbh	unverified	0	allemagne	1	0.0

68	new 2wd gasoline engine power rotary tiller multifunction agricultural machinery with core gearbox for farm home use & retail	1	50	68	1		0	0.0	0.0	0.0	0.0	1	1	1	1	185.0	185.0	taizhou hongfu commercial and trading co., ltd.	unverified	0	chine	1	0.0

69	agricultural machinery & equipment chaff cutter dry grass fine chaff cutter machine	1	1	69	1		0	0.0	0.0	0.0	0.0	1	1	1	1	140.0	155.0	shuangfeng jinnongbao agricultural machinery co., ltd.	unverified	0	chine	1	0.0

70	new products gasoline rotary tiller soil cultivator plowing agricultural machine for farm	1	1	70	1		0	5.0	2.0	5.0	5.0	1	1	1	1	2400.0	3200.0	qingzhou zhongwei agricultural machinery co., ltd.	unverified	2	chine	1	5.0

71	pto driven long grass cutter heavy verge flail mower heavy flail mower machine tractor farm tractor agricultural machinery	1	5	71	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1300.0	1300.0	changzhou qianyi machinery technology co., ltd.	unverified	0	chine	1	0.0

72	tractors, agricultural machinery, tractor 4-wheel drive, 50 horsepower	1	1	72	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6500.0	6500.0	xinxiang hongmao machinery equipment co., ltd.	unverified	0	chine	1	0.0

73	good price cow poultry feed pellet machine	1	2	73	1		0	4.2	27.0	4.1	4.2	1	1	1	1	498.0	498.0	anping county yize metal products co., ltd.	unverified	3	chine	12	4.0

74	pinyang millet peeling machine buckwheat quinoa sheller machine for sales	1	1	74	1		0	3.8	6.0	4.0	4.0	1	1	1	1	7500.0	7500.0	hubei pinyang technology co., ltd.	unverified	3	chine	6	4.3

75	multi function paddy harvesting and bundling machine wheat harvesting machine rice harvester	1	1	75	1		1	5.0	17.0	5.0	5.0	1	1	1	1	2200.0	3900.0	henan domax machinery co., ltd.	unverified	2	chine	1	5.0

76	joyance high productivity window cleaning drone powerful machine for glass curtain wall washing factory direct from china	1	1	76	1	CE	0	5.0	21.0	5.0	5.0	1	1	1	1	5500.0	7200.0	shandong joyance intelligence technology co., ltd.	unverified	3	chine	8	5.0

77	flexible screw conveyor grain suction vacuum pump machine for grain	1	1	77	1		10	4.8	8.0	4.8	4.8	1	1	1	1	255.0	280.0	xinxiang dahan vibrating machinery co., ltd.	unverified	3	chine	11	4.8

78	seesa new 80l/100l wheel barrow agriculture electric powered pump plant sprayer machine	1	10	78	1		0	5.0	3.0	5.0	5.0	1	1	1	1	277.0	292.0	shixia holding co., ltd.	unverified	3	chine	22	5.0

79	agriculture soil bed former ridger best quality farm tractor ridge making ridges machine 1~3 rows ridging machine	1	1	79	1		2	3.3	4.0	3.8	4.2	1	1	1	1	1000.0	4115.0	jiangsu jitian international trade co., ltd.	unverified	1	chine	5	4.0

80	wholesale price linear pivot irrigation machine for water irrigation	1	1	80	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6000.0	6000.0	dalian gengze agricultural equipment manufacturing co., ltd.	unverified	1	chine	6	0.0

81	new design 200 tpd capacity combined full automatic rice mill plant color sorter machine manufacturer china	1	1	81	1		0	5.0	2.0	5.0	5.0	1	1	1	1	19850.0	19850.0	hefei longbow optoelectronic technology co., ltd.	unverified	2	chine	6	5.0

82	high quality small celery harvester leaf vegetable harvester vegetable leafy harvester machine for agricultural products	1	1	82	1		2	5.0	30.0	5.0	5.0	1	1	1	1	800.0	2000.0	henan joconn machinery co., ltd.	unverified	2	chine	6	5.0

83	sesame harvesting machine	1	1	83	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7500.0	15000.0	royermak makina ic ve dis ticaret limited sirketi	unverified	2	turquie	6	0.0

84	stable performance cow dung solid-liquid separator / biogas slurry dewatering machine	1	1	84	1		0	5.0	18.0	5.0	5.0	1	1	1	1	1450.0	1450.0	zhengzhou hongle machinery equipment co., ltd.	unverified	4	chine	15	5.0

85	high quality home rice mill machine thailand mini rice mill milling machine rice husk hammer mill machine	1	1	85	1		0	4.0	5.0	4.0	4.0	1	1	1	1	169.0	249.0	sichuan xingsida mechanical and electrical manufacturing co., ltd.	unverified	0	chine	6	4.2

86	brands 4x4 50hp farm tractors agriculture tractor with environmental protection engine 4wd small mini tractor	1	1	86	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6180.0	6303.0	shandong luyu intelligent equipment co., ltd.	unverified	0	chine	2	0.0

87	good quality laverda new holland maize harvesting corn harvest machine combine harvester for sale	1	1	87	1		0	4.6	9.0	4.6	4.5	1	1	1	1	66600.0	68600.0	zhengzhou meijin machinery equipment co., ltd.	unverified	1	chine	1	4.7

88	millet/ rice/ beans/ wheat/ maize debris cleaning machine	1	1	88	1		0	4.1	11.0	4.3	4.5	1	1	1	1	700.0	700.0	zhengzhou yingwang machinery co., ltd.	unverified	1	chine	9	4.4

89	2l 2000 to kill mosquito pest control fumigation sprayer mini thermal fogger machine	1	1	89	1		1	4.7	7.0	4.7	4.7	1	1	1	1	39.0	50.0	taizhou aodisen machinery co., ltd.	unverified	0	chine	1	4.8

90	multifunctional seed sorting granule powder vibrating screen impurity separator grain cleaning vibration screening machine	1	1	90	1		0	5.0	3.0	5.0	5.0	1	1	1	1	241.0	278.0	xiamen greatbond technology co., ltd.	unverified	0	chine	4	5.0

91	1lzx suspension type unites entire machine	1	1	91	1		0	0.0	0.0	0.0	0.0	1	1	1	1	60.0	60.0	shandong yuntai machinery co., ltd.	unverified	1	chine	19	0.0

92	multi-functional soybean corn sheller and thresher machine	1	1	92	1		0	0.0	0.0	0.0	0.0	1	1	1	1	353.0	483.0	phoenix industry company limited.	unverified	0	chine	7	0.0

93	high quality professional tractor trencher ditcher for farm digging machine	1	1	93	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1200.0	1500.0	shandong gaotang xinhang machinery co., ltd.	unverified	1	chine	8	5.0

94	agricultural forage pickup baler corn straw baler full automatic green storage feed harvesting baler on sale	1	1	94	1		0	5.0	7.0	5.0	5.0	1	1	1	1	1800.0	2200.0	zhengzhou qiongdan machinery co., ltd.	unverified	1	chine	6	5.0

95	multifunctional agriculture green farm use silage cow feed grass chaff cutter machine animal feed crushing grain machine	1	1	95	1		2	4.7	43.0	4.6	4.4	1	1	1	1	240.0	260.0	dongguan haixingda machinery co., ltd.	unverified	2	chine	1	4.7

96	15hp - 230hp agricultural machinery 4wd mini tractor with cabin multifunction mini tractor	1	2	96	1		0	4.4	108.0	4.4	4.3	1	1	1	1	980.0	980.0	shandong nuote machinery co., ltd.	verified	5	chine	4	4.4

97	lawn mower knapsack brush cutter farm weeding machine agriculture machinery	1	1	97	1		0	4.4	12.0	4.5	4.5	1	1	1	1	85.0	95.0	henan zealyu machinery co., ltd.	unverified	1	chine	5	4.6

98	cultivation suppliers agricultural machinery equipment and tools cultivation agricultural machinery co ltd	1	1	98	1		0	5.0	3.0	5.0	5.0	1	1	1	1	800.0	800.0	weifang shengchuan machinery co., ltd.	unverified	1	chine	11	5.0

99	chalion brand 4x4 mini tractor 60hp 65hp 70hp 75hp 80hp 90hp tractor agricultural machinery with yto diesel engine price	1	1	13	1	CE	0	5.0	8.0	5.0	5.0	1	1	1	1	9000.0	9000.0	jinan demeijia machinery co., ltd.	unverified	3	chine	10	4.9

100	mini agriculture machinery tractor corn maize harvester machine/maize combine harvester equipment small harvest machine	1	1	14	1	CE	26	4.8	124.0	4.7	4.7	1	1	1	1	1900.0	2000.0	taian taishan guotai tractor manufacturing co., ltd.	unverified	0	chine	9	0.0

101	28hp farming agricultural machinery plow	1	1	99	1		0	4.9	41.0	4.9	4.9	1	1	1	1	399.0	499.0	hebei helida grain selecting machinery technology co., ltd.	unverified	2	chine	9	5.0

102	hydraulic adjustable turn over plow farming tractor agricultural machinery	1	1	100	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	6000.0	hebei lubing technology co., ltd.	unverified	2	chine	2	4.7

103	agricultural machinery & equipment seed cleaner	1	1	101	1		0	5.0	3.0	5.0	5.0	1	1	1	1	4963.0	5036.0	henan foya machinery co., ltd.	unverified	1	chine	5	5.0

104	hot seal diesel chain rail type small micro-tiller agricultural plowing and tilling machine small agricultural tillage machinery	1	1	102	1		61	4.9	38.0	4.9	4.9	1	1	1	1	240.6	240.6	henan formend imp. & exp. co., ltd	unverified	1	chine	8	5.0

105	manufacturer tractor agriculture machinery grass cutter drum hay mower	1	1	47	1		0	4.4	13.0	4.3	4.3	1	1	1	1	600.0	960.0	qingdao hans machinery technology co., ltd.	unverified	2	chine	4	3.8

106	single row potato/ peanut /ginger /garlic combine harvester/modern agricultural machinery for sale	1	1	103	1		0	4.7	3.0	4.8	4.6	1	1	1	1	1025.0	1355.0	eurl sarl aliop	unverified	2	france	2	0.0

107	mini tiller cultivator agricultural machine in china agricultural equipment for sale	1	1	104	1		0	5.0	17.0	4.9	4.9	1	1	1	1	425.0	465.0	qingdao lermda import and export co., ltd.	unverified	1	chine	4	4.8

108	easy to use and high efficient agricultural machinery/walking tractor with various of complement/agricultural equipment hot sale	1	1	105	1		1	4.6	29.0	4.2	4.1	1	1	1	1	580.0	720.0	geg okostrom gmbh	unverified	2	autriche	2	0.0

109	tx tiller machine agricultural diesel gasoline loose soil furrow ridge subsoiler weeding mini power tiller rotary cultivator	1	1	33	1		0	5.0	7.0	5.0	5.0	1	1	1	1	115.0	125.0	henan unio machinery co., ltd.	unverified	2	chine	2	4.2

110	massey ferguson 6615 dyna tractors agricultural machinery & equipment	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	k&f machinery ltd.	unverified	0	chine	1	0.0

111	used agricultural machinery & equipment/farm tractor/good quality used fendt 927 vario tractor	1	1	37	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	jm  solozabal services llc	unverified	2	�tats-unis	1	0.0

112	guaranteed quality agricultural machinery rotary tiller cultivator	1	1	107	1		0	4.8	8.0	4.7	4.5	1	1	1	1	400.0	415.0	bauducco	unverified	2	�tats-unis	2	0.0

113	fairly used agriculture machinery combine harvester for affordable price rice and wheat combine harvester for sale	1	1	108	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1999.0	1999.0	wuhan xinkai machinery co., ltd.	unverified	1	chine	7	4.2

114	agriculture machinery combine harvester for rice and wheat combine harvester for corn wheat grains cotton available for low cost	1	1	22	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7000.0	8000.0	wuhan anon tech trade co., ltd.	unverified	1	chine	12	5.0

115	groundnut/peanut sheller machine thresher ground nut sheller manual agricultural machinery shellers peanut peeling machine price	1	1	109	1		1	4.1	40.0	4.2	4.3	1	1	1	1	479.0	529.0	yantai lansu measurement and control instrument co., ltd.	unverified	4	chine	8	5.0

116	high quality plastic film mulching machine film layer machine small agriculture machinery for farm filed orchard garden	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	480.0	550.0	taian jiyi machinery equipment co., ltd.	unverified	1	chine	3	4.9

117	claas 950 combine harvester/ fairly used agriculture machinery combine harvester	1	1	111	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8000.0	10000.0	yongkang cosmos machinery co., ltd.	unverified	0	chine	14	0.0

118	agricultural machinery, farm machinery equipment agricultural tractor 4x4 mini farm 4wd compact tractor	1	1	112	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6400.0	7000.0	yantai dibo machinery equipment co., ltd.	unverified	3	chine	4	5.0

119	tractor mounted boom sprayer agricultural machinery for sale	1	1	113	1		0	4.2	5.0	4.3	4.8	1	1	1	1	700.0	800.0	jiashan jianyi machinery co., ltd.	unverified	1	chine	3	4.8

120	anon agriculture spray machine boom sprayer agricultural machinery	1	1	114	1		0	5.0	5.0	4.7	4.2	1	1	1	1	1210.0	1300.0	qingdao wonshiner agricultural technology co., ltd.	unverified	3	chine	2	4.8

121	agricultural machinery/hot sale / mini /small/compact diesel engine/electric 2 wheel walking tractor	1	1	115	1	CE	0	5.0	2.0	5.0	5.0	1	1	1	1	200.0	200.0	cradle and bloom ltd	unverified	2	royaume-uni	1	0.0

122	high quality original combine harvester rice wheat new condition core engine component affordably priced agriculture machinery	1	1	116	1		0	4.9	31.0	4.9	5.0	1	1	1	1	3800.0	4000.0	shandong h. t-bauer water and agricultural machinery & engineering co., ltd.	unverified	0	chine	13	0.0

123	20 liter knapsack power mist sprayer agriculture machine on sale	1	1	32	1		0	5.0	1.0	5.0	5.0	1	1	1	1	20.9	22.1	india agrovision implements private limited	unverified	2	inde	4	0.0

124	reasonable price high quality 13hp two wheel walking tractor power tiller micro tractor small agricultural machine	1	10	117	1		0	0.0	0.0	0.0	0.0	1	1	1	1	650.0	680.0	qingdao henry industry co., ltd.	unverified	1	chine	14	5.0

125	agricultural machinery 45hp farm tractors for agriculture	1	1	19	1		0	4.8	9.0	4.7	4.6	1	1	1	1	4800.0	5600.0	shandong tavol machinery co., ltd.	unverified	1	chine	5	4.2

126	manual/recoil stepless full gear one year gasoline motorcycle agriculture machinery mini spare parts electric garden tiller	1	1	118	1		0	5.0	11.0	5.0	5.0	1	1	1	1	264.0	312.0	jmso group llc	unverified	2	�tats-unis	1	0.0

127	agricultural machinery diesel 4x4 new tractor agriculture traktor plowing machine wheel tractor	1	1	119	1		0	4.8	12.0	4.8	4.8	1	1	1	1	2009.0	2498.0	shandong zhuoqi machinery technology co., ltd.	unverified	0	chine	5	2.3

128	agriculture machinery combine harvester 102 hp for rice and wheat used world combine harvester kubota combine harvester japan	1	1	120	1		0	4.8	36.0	4.8	4.7	1	1	1	1	4000.0	4000.0	ifourni technology co., ltd	unverified	1	chine	4	4.8

129	original quality agriculture machinery combine harvester for rice and wheat cheap combine harvester available	1	1	121	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0	linyi yunfan comprehensive agricultural development co., ltd.	unverified	1	chine	4	1.0

130	china agricultural machinery and pivot prices in egypt	1	1	122	1		0	0.0	0.0	0.0	0.0	1	1	1	1	13000.0	20000.0	shijiazhuang tianren agricultural machinery equipment co., ltd.	unverified	0	chine	11	5.0

131	best quality front end loader use farm tractor best agricultural machinery at latest discounted price	1	1	123	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2090.0	2682.0	shandong haichuan environmental protection technology co., ltd.	unverified	1	chine	1	5.0

132	low price agriculture machinery combine harvester for rice and wheat	1	1	124	1		0	5.0	6.0	5.0	5.0	1	1	1	1	4200.0	5000.0	henan volun machinery co., ltd.	unverified	1	chine	5	0.0

133	agriculture machinery combine harvester for rice and wheat rice harvester mini combine harvester for sale	1	1	125	1		0	4.3	5.0	4.5	5.0	1	1	1	1	122500.0	123000.0	tianjin qiangbang industrial co., ltd.	unverified	4	chine	11	5.0

134	cheap agriculture machinery claas 960 combine harvester/ fairly used agriculture machinery combine harvester	1	1	126	1		0	0.0	0.0	0.0	0.0	1	1	1	1	27000.0	27000.0	yancheng dafeng longjiang machinery factory	unverified	0	chine	18	0.0

135	second used massey ferguson baler mf1840 agricultural machinery for sale packing bander agricultural equipment farm land 680-770	1	1	127	1		0	1.8	3.0	2.1	2.3	1	1	1	1	10300.0	10500.0	yongkang powertec import & export co., ltd.	verified	1	chine	18	0.0

136	farming equipment agricultural machinery cow dung dewatering machine	1	1	39	1		0	4.5	2.0	4.5	4.5	1	1	1	1	1718.0	1773.0	shijiazhuang synmec international trading limited	verified	2	chine	11	5.0

137	ifourni 15l agricultural spray machine knapsack gasoline pesticide petrol motor power sprayer agriculture machine 2 stroke motor	1	1	128	1		0	4.7	37.0	4.7	4.7	1	1	1	1	49.9	56.4	rovu trade gmbh	unverified	2	allemagne	1	0.0

138	two way disc plough other agricultural machinery&equipment	1	1	129	1		6	1.0	1.0	1.0	1.0	1	1	1	1	950.0	1000.0	zhengzhou weiwei machinery co., ltd.	verified	2	chine	9	4.7

139	agricultural machine and farm equipment corn rice wheat combine harvester	1	1	130	1		0	5.0	1.0	5.0	5.0	1	1	1	1	81000.0	82000.0	hebei sujie bike co., ltd.	unverified	3	chine	4	5.0

140	25hp small 4x4 farm tractor farm use mini tractor agricultural tractor agriculture machine	1	1	131	1		0	5.0	17.0	5.0	5.0	1	1	1	1	2900.0	3000.0	bright future international trading(dalian) co., ltd.	unverified	0	chine	7	5.0

141	agriculture machinery 3 point disc plough mounted with farm tractor/1lyq-220 2 disc plow	1	1	132	1		0	0.0	0.0	0.0	0.0	1	1	1	1	500.0	1000.0	zhengzhou wutong machinery equipment co., ltd.	unverified	1	chine	3	5.0

142	disc plough/scarifier/four-wheel tractor drive soil tillage drive disc plough agricultural machine	1	3	133	1		0	5.0	4.0	5.0	5.0	1	1	1	1	250.0	350.0	shijiazhuang fineyou trade co., ltd.	unverified	1	chine	7	0.0

143	agricultural machinery, an agricultural equipment tool for all kinds of power matchingpower tiller	1	3	134	1		0	0.0	0.0	0.0	0.0	1	1	1	1	670.0	703.0	jilin yaoda machinery equipment co., ltd.	unverified	0	chine	2	5.0

144	new designed agricultural machinery and equipment gasoline tiller cultivator power tillers	1	500	135	1		100	0.0	0.0	0.0	0.0	1	1	1	1	186.59	195.47	henan enrun new materials co., ltd.	unverified	0	chine	1	0.0

145	agriculture machinery equipment de-stoner rice stoner rice cleaning machine	1	1	136	1		0	5.0	5.0	5.0	5.0	1	1	1	1	3000.0	3000.0	nl holding gmbh	unverified	3	allemagne	1	0.0

146	buy original quality agriculture machinery combine harvester for rice and wheat cheap combine harvester available for sale	1	1	137	1		0	0.0	0.0	0.0	0.0	1	1	1	1	17500.0	17500.0	weifang kafan industrial technology co., ltd.	unverified	0	chine	1	0.0

147	latest agricultural machine how to make chaff grass cutting machine in chennai classic industry	1	1	138	1		1	4.9	23.0	4.7	4.7	1	1	1	1	150.0	680.0	xuchang shengte trade co., ltd.	unverified	1	chine	9	5.0

148	grain paddy multifunction mobile agricultural machinery farm equipment 5xfz-15bx comblned seed cleaning processing machine	1	1	139	1		0	5.0	2.0	5.0	5.0	1	1	1	1	6000.0	7000.0	jiangsu grande machinery manufacturing co., ltd.	unverified	2	chine	4	5.0

149	bcs technology two-wheel tractors agricultural machinery 9.0hp diesel motor with attached swivel rotary plow ce approved	1	1	140	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1953.0	2153.0	zhengzhou guandu machinery equipment co., ltd.	unverified	1	chine	8	3.8

150	agriculture machinery equipment peanut picker groundnut picking machine price	1	1	141	1		0	5.0	2.0	5.0	5.0	1	1	1	1	500.0	500.0	shandong stabili farm machine co., ltd.	unverified	0	chine	3	5.0

151	fineyou small agriculture machine one row corn picker mini walking tractor single row maize harvesting machines	1	1	142	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1100.0	1360.0	xinji wonong agricultural machinery sales co., ltd.	unverified	0	chine	1	0.0

152	self-propelled sprayer agricultural fertilizer agricultural chemicals spraying system tractor pulled machine 3000l tank volume	1	1	143	1		0	5.0	1.0	5.0	5.0	1	1	1	1	130000.0	130000.0	jining aowei machine co., limited	unverified	2	chine	5	4.4

153	agriculture machine gasoline power cultivator weeding machine mini power weeder hand weeder tool hand held weeding machine	1	1	144	1		0	0.0	0.0	0.0	0.0	1	1	1	1	88.0	88.0	guangxi shuanggao agricultural machinery co., ltd.	unverified	0	chine	3	0.0

154	new self propelled agricultural sprayer pesticide tractor mounted boom sprayer agricultural machinery for corn	1	1	146	1		0	0.0	0.0	0.0	0.0	1	1	1	1	14500.0	15500.0	tianjin shuofan agriculture tecknology co., ltd.	unverified	0	chine	1	0.0

155	agricultural machinery farm tractor stone picker machine stone separating machine for sales	1	1	119	1		0	4.8	12.0	4.8	4.8	1	1	1	1	999.0	1599.0	ent so-grind	unverified	2	france	1	0.0

156	direct factory operation home use 5tg-80 paddy thresher threshing machine for wheat sorghum agriculture machinery	1	1	116	1		1	4.9	31.0	4.9	5.0	1	1	1	1	390.0	400.0	shandong ling ke imp and exp co., ltd.	unverified	3	chine	1	5.0

157	hot selling agricultural use chaff cutter machine in kenya chaff cutter machine animal feed electric chaff cutter	1	1	147	1		16	5.0	7.0	4.9	4.8	1	1	1	1	213.0	226.0	dezhou yasheng agricultural machinery co., ltd.	unverified	1	chine	1	5.0

158	agricultural machinery paddy rice processing equipment price rice milling machine sb-5 in cheap price	1	1	148	1		0	5.0	12.0	5.0	5.0	1	1	1	1	580.0	880.0	dongguan strong machinery equipment co., ltd.	unverified	1	chine	1	5.0

159	agricultural machinery /west africa power tiller hot sale pricegasoline generator hf-180cfs	1	1	149	1		0	3.8	58.0	3.7	3.6	1	1	1	1	318.0	388.0	leshan tianqin agricultural machinery co., ltd.	unverified	2	chine	1	4.7

160	newly arrival best quality front end loader heavy duty equipment supplier use agricultural machinery	1	1	123	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2090.0	2682.0	bada (shandong) agricultural machinery co., ltd.	unverified	3	chine	3	4.6

161	agricultural machine implement 3 disc plough for tractors	1	1	19	1		3	4.8	9.0	4.7	4.6	1	1	1	1	265.0	280.0	shandong unio machinery equipment co., ltd.	unverified	1	chine	1	3.0

162	massey ferguson 175 agricultural machinery / new 85hp farm tractor	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3500.0	linyi ronglian machinery co., ltd.	unverified	1	chine	2	0.0

163	silage baler agricultural machinery silage bagger silage maker machine film wrapping machine	1	1	103	1		0	4.7	3.0	4.8	4.6	1	1	1	1	2450.0	2650.0	asap immobilier	unverified	2	france	1	0.0

164	second hand tractors john 5e-954 deere 95hp for sale cheap farm tractors agricultural machinery from china	1	1	120	1		0	4.8	36.0	4.8	4.7	1	1	1	1	9750.0	9750.0	35 funfunddreisig gmbh	unverified	1	autriche	2	0.0

165	used tractors deutz fahr 100hp 4x4wd compact orchard farm two wheel german agricultural machinery	1	1	150	1		0	5.0	1.0	5.0	5.0	1	1	1	1	9500.0	10000.0	qingdao nuts machinery co., ltd.	unverified	2	chine	3	4.5

166	45hp 50hp 55hp 60hp 70hp tractor wheel tractor agriculture machinery	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6200.0	6600.0	yiwu lifeng machinery equipment co., ltd	unverified	2	chine	2	4.3

167	zongshen high quality lightweight gasoline rotary tiller easy-to-operate agricultural machinery soil loosening cultivators	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	206.02	303.11	yucheng yuming machinery co., ltd.	unverified	1	chine	6	4.4

168	good rice seeders and transplanters used agricultural machines	1	1	36	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	15000.0	shandong wonway machinery co., ltd.	unverified	5	chine	3	4.4

169	tractors for agricultural rice fields agricultural machinery for cutting grass and cultivated land multi-purpose tractors	1	1	152	1		2	4.5	12.0	4.4	4.5	1	1	1	1	980.0	980.0	vif gerustbau gmbh	unverified	1	autriche	2	0.0

170	sugarcane planting machine sugarcane agricultural machine sell in philippines	1	1	153	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1999.0	2300.0	henan nkun machinery co., ltd.	unverified	2	chine	5	4.5

171	electric self-propelled weeding and cultivating tractor turns soil and ditches multifunctional agricultural machine	1	1	109	1		0	4.1	40.0	4.2	4.3	1	1	1	1	99.0	119.0	chongqing changbaotian machinery technology co., ltd.	unverified	2	chine	2	4.6

172	new agricultural machinery plough disc agricultural disc plough 3 disc plough mold plow	1	1	119	1		0	4.8	12.0	4.8	4.8	1	1	1	1	530.0	580.0	anshan anza electronic power co., ltd.	unverified	1	chine	3	4.0

173	hot selling agricultural machinery cultivators low-priced machines high-quality packaging machines	1	1	154	1		0	0.0	0.0	0.0	0.0	1	1	1	1	20000.0	20000.0	jmp trade og	unverified	4	autriche	1	0.0

174	tx cheap agricultural machinery mini hand tiller machine agricultural walking tractor power tiller 6hp cultivator rotary tiller	1	5	33	1		0	5.0	7.0	5.0	5.0	1	1	1	1	220.0	240.0	changzhou hantechn imp. & exp. co., ltd.	verified	3	chine	8	4.8

175	buy cheap massey ferguson 390 agricultural machinery / used 1580hp mf390 farm tractor available for sale	1	1	155	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	3000.0	henan yulu machinery co., ltd.	verified	3	chine	4	5.0

176	production and sales of light and medium-sized heavy gear chain drive agricultural machinery rotary tiller	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	452.0	452.0	renqiu yu qilin textile agricultural machine co., ltd.	unverified	1	chine	19	5.0

177	agriculture machinery farm tractor 3 point pto rotary tiller	1	1	156	1		0	5.0	2.0	5.0	5.0	1	1	1	1	358.0	358.0	huangshi eason technology co., ltd.	unverified	2	chine	5	5.0

178	used agricultural machinery & equipment/farm tractor/good quality used fendt tractor	1	1	48	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2800.0	liyang yuda machinery co., ltd.	unverified	0	chine	8	0.0

179	wholesale agricultural machine tractor disc plow disc plough for sale	1	1	157	1		0	5.0	2.0	5.0	5.0	1	1	1	1	730.0	820.0	3 bruder a gmbh	unverified	1	autriche	2	0.0

180	177f/p mini power tiller 7hp 9hp cultivator power tiller machine with attachments price agricultural gasoline diesel tiller	1	1	118	1		3	5.0	11.0	5.0	5.0	1	1	1	1	370.0	396.0	shijiazhuang huanpai machine co., ltd.	unverified	0	chine	16	0.0

181	tractors mini 4x4 30hp 40hp 50hp 4 drive tractor best price agricultural farming mini tractor 4x4 for sale	1	1	96	1		28	4.4	108.0	4.4	4.3	1	1	1	1	1280.0	1280.0	auto memishoski og	unverified	2	autriche	1	0.0

182	mini self propelled power cultivator small plough machine gasoline and diesel engine plough machine	1	1	158	1		0	5.0	2.0	5.0	5.0	1	1	1	1	169.0	487.0	luoyang haryst trading co., ltd.	unverified	2	chine	2	4.2

183	peanut picking machine / groundnut picker / peanut harvester	1	1	132	1		0	0.0	0.0	0.0	0.0	1	1	1	1	800.0	1999.0	luoyang luodate machinery equipment co., ltd.	unverified	2	chine	11	5.0

184	hot selling corn husk peeling wheat skin peeling machine crops skin removing machine milliet kernels peeler	1	1	14	1		2	4.8	124.0	4.7	4.7	1	1	1	1	595.0	595.0	sanmenxia weiyi agricultural machinery sales co., ltd.	unverified	2	chine	7	5.0

185	manual hand push corn embradora de maiz manual corn planter machine 1 row seeder hand push seeder machine planter	1	1	128	1		3	4.7	37.0	4.7	4.7	1	1	1	1	43.0	45.0	gaoyang county tianhui agricultural machinery spare parts sale agent	unverified	0	chine	14	0.0

186	agricultural machinery single row harvester sweet potato harvester potato digger	1	1	107	1		0	4.8	8.0	4.7	4.5	1	1	1	1	550.0	600.0	longyan yilin shangye e-commerce co., ltd.	unverified	0	chine	1	5.0

187	professional moving easily multifunctional thresher machine paddy wheat soy bean sorghum bb-tw40	1	1	159	1		2	4.8	19.0	4.7	4.7	1	1	1	1	188.0	218.0	luohe nine lemon import & export co., ltd.	unverified	3	chine	5	4.6

188	agricultural implement tractors attachments hydraulic reversible turning plough machine for tractor	1	1	160	1		0	4.8	3.0	4.7	4.6	1	1	1	1	580.0	580.0	dezhou panda machinery co., ltd.	unverified	0	chine	8	5.0

189	anon agriculture machinery equipment 2 wheel farm walking tractor	1	2	114	1		0	5.0	5.0	4.7	4.2	1	1	1	1	500.0	1500.0	zhengzhou huamo machinery equipment co., ltd.	unverified	0	chine	2	5.0

190	2023 high quality tavol cabin fram tractor agriculture 150hp tractor for farming working	1	1	125	1		0	4.3	5.0	4.5	5.0	1	1	1	1	12300.0	13000.0	leshan san yuan electrical machinery co., ltd.	unverified	0	chine	5	0.0

191	lisa heavy duty rotary tiller 3 point linkage tractor 30~50 hp farm tilling machine agriculture tools equipment pto rotary power	1	1	161	1		1	3.6	2.0	3.2	3.0	1	1	1	1	419.0	469.0	zhejiang menghua sprayer co., ltd.	unverified	0	chine	16	0.0

192	second hand tractors new snh 704 holland 70 hp used tractors for agriculture	1	1	162	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2800.0	6200.0	shijiazhuang mangteng electromechanical equipment sales co., ltd.	unverified	0	chine	6	4.5

193	used mini kubota 4wd 4x4 20hp 50hp 25hp 120hp mini farm tractors used kuboota agriculture farm machinery cheap farm tractor	1	1	163	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1050.0	1050.0	anhui heavy and light industries international co., ltd.	unverified	5	chine	4	5.0

194	original uk kubota tractor available for sale agricultural machinery tractors used and new cheap price	1	1	164	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2150.0	2150.0	zhengzhou well-known instrument & equipment co., ltd.	unverified	3	chine	4	5.0

195	agricultural machinery multifunction 2wd gasoline engine power tiller motor cultivator	1	1	47	1		1	4.4	13.0	4.3	4.3	1	1	1	1	180.0	210.0	weifang tianying machinery co., ltd.	unverified	0	chine	8	0.0

196	agricultural machinery small mini 4x4 compact farm tractor	1	1	165	1		45	4.3	8.0	4.5	4.6	1	1	1	1	1300.0	2500.0	chongqing xiaostepu technology co., ltd.	unverified	0	chine	1	0.0

197	professional agriculture weeding machine power weeder hand held weeding machine mini gasoline power weeder motor provided farm	1	1	166	1		0	4.2	16.0	4.2	4.1	1	1	1	1	90.0	150.0	fujian century sea power co., ltd.	unverified	3	chine	13	5.0

198	case tractor 650hp case ih agricultural tractor available at wholesale price	1	1	79	1		0	3.3	4.0	3.8	4.2	1	1	1	1	84000.0	85000.0	chongqing huitian machinery manufacturing co., ltd.	unverified	0	chine	15	0.0

199	1l series light duty farm share plough/3 point hitch provided plough machine farm cultivator agricultural farm machinery plough	1	1	167	1		0	4.6	10.0	4.4	4.4	1	1	1	1	160.0	190.0	hangzhou mory trade co., ltd.	unverified	0	chine	10	5.0

200	multifunctional farming machine remote control rotary cultivator agriculture machinery equipment small tractor tiller	1	1	168	1		1	4.5	125.0	4.4	4.3	1	1	1	1	1100.0	1100.0	zhengzhou yize machinery co., ltd.	unverified	3	chine	9	4.7

201	cheap massey ferguson tractor 385 mf 290 mf 399 and mf 455 extra agriculture machine farm tractor for sale	1	1	169	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2250.0	2250.0	zhengzhou golmyt machinery co., ltd.	unverified	0	chine	4	5.0

202	mist blower sprayers agriculture machinery equipment sprey pump self propelled tractor sprayer	1	1	170	1		0	4.8	6.0	4.6	4.6	1	1	1	1	3000.0	4500.0	organic farm gmbh	unverified	2	allemagne	3	0.0

203	changtian industrial sprayer agricultural mist garden plant boom sprayer pump agricultural backpack sprayer	1	1	171	1		1	4.1	65.0	4.4	4.4	1	1	1	1	58.0	90.0	qingdao ablson machinery co., ltd.	unverified	2	chine	12	5.0

204	special hot selling mini rotary tiller small agricultural machine cultivator gasoline tillers motor multifunctional provided 88	1	1	116	1		0	4.9	31.0	4.9	5.0	1	1	1	1	500.0	500.0	dongguan city strong machinery co., ltd.	unverified	1	chine	1	4.0

205	china agriculture machine motocultor garden farm 12hp 15hp 18hp diesel two wheel walk behind cultivator rotary mini power tiller	1	1	172	1		0	3.6	2.0	4.0	4.5	1	1	1	1	450.0	520.0	xuzhou kat agricultural equipment co., ltd.	unverified	0	chine	15	0.0

206	buy good condition combine harvester agricultural machinery maize wheat rice grain harvester machine	1	1	173	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9000.0	9000.0	jbk manufacturing and development company	unverified	0	�tats-unis	3	0.0

207	wholesale gasoline mini power tiller factory price agricultural machinery equipment cultivator trailer 51.7cc mini rotary tiller	1	1	174	1		1	4.9	21.0	4.9	4.9	1	1	1	1	58.0	80.0	wuhan acme agro-tech co., ltd.	unverified	0	chine	14	4.3

208	farming small agriculture machinery power tilelr tiller cultivator garden orchard greenhouse equipment	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	300.0	320.0	yucheng tianming machinery co., ltd.	verified	0	chine	16	4.8

209	yg 25hp agricultural machinery tractor sugarcane rotary tiller sugar cane cultivator	1	1	175	1		0	5.0	7.0	5.0	5.0	1	1	1	1	4000.0	5500.0	sci les charmilles	unverified	2	france	2	0.0

210	used tractor 90hp second hand tractor second agriculture machinery	1	1	176	1		0	4.9	8.0	4.8	4.6	1	1	1	1	3500.0	13000.0	yancheng harriston int'l co., ltd.	unverified	2	chine	8	4.6

211	t40 new trending tractor mounted stem borer sprayer,grapery pvc farm shadow machine agriculture hoses machines	1	1	177	1		0	5.0	13.0	4.9	4.9	1	1	1	1	5299.0	5299.0	yucheng future agriculture machinery co., ltd.	unverified	1	chine	4	0.0

212	yuda factory small scale machinery agricultural machinery equipment feed processing machines	1	1	178	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6200.0	7500.0	luoyang dragon-horse machinery co., ltd.	unverified	0	chine	15	5.0

213	agriculture machinery combine harvester for rice and wheat cheap price	1	2	179	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	6000.0	shandong hualong agricultural equipment co., ltd.	unverified	0	chine	9	0.0

214	agriculture machinery equipment mixer animal feed machine feed processing machines	1	1	180	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	quanzhou jingli engineering and machinery co., ltd.	unverified	2	chine	7	0.0

215	fairly used new holland tc5070 combine harvester agricultural machinery for sale tc5070	1	1	181	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8000.0	8000.0	jiaxing norsun trading co., ltd.	unverified	3	chine	11	4.8

216	agricultural machinery precision corn seeder machine for sale	1	1	113	1		0	4.2	5.0	4.3	4.8	1	1	1	1	6000.0	6500.0	ogruc immobilien gmbh	unverified	0	autriche	2	0.0

217	hot-selling small agricultural machine/mini tiller cultivator 6.12 horsepower power tiller agricultural equipment	1	1	182	1		0	4.2	5.0	4.3	4.6	1	1	1	1	370.0	417.0	trading-b b.v.	unverified	3	pays-bas	2	0.0

218	manufacturer for small animal feed processing machine/cattle feed plant/agricultural machinery equipment	1	1	183	1		0	5.0	3.0	5.0	5.0	1	1	1	1	15000.0	20000.0	shanghai land universal machinery equipment co., ltd.	unverified	1	chine	1	5.0

219	agriculture machinery combine harvester for rice and wheat combine harvester	1	1	111	1		0	0.0	0.0	0.0	0.0	1	1	1	1	10000.0	10000.0	shandong qihang agricultural machinery co., ltd	unverified	2	chine	3	4.3

220	small farm machines atv cultivator mtoculteur cultivators agricultural machines	1	1	184	1		0	4.7	31.0	4.8	4.7	1	1	1	1	250.0	772.0	jinan synbon machinery electronics co., ltd.	unverified	0	chine	4	5.0

221	china supply high quality agricultural machinery yf-16 rice husker	1	100	185	1		0	0.0	0.0	0.0	0.0	1	1	1	1	60.0	120.0	guohaha agricultural machinery (shandong) co., ltd.	unverified	1	chine	2	0.0

222	new agricultural machinery 60hp multifunction mini crawler cultivator for sale	1	1	168	1		0	4.5	125.0	4.4	4.3	1	1	1	1	1400.0	1500.0	shandong horse agricultural equipment co., ltd.	unverified	1	chine	1	5.0

223	agricultural machinery diesel/gasoline small tractor plowing/ditching/loosening/tilling automatic other engine two stroke 18hp	1	1	186	1		0	5.0	5.0	5.0	5.0	1	1	1	1	126.0	600.0	linyi zhonghe international trade co., ltd.	unverified	1	chine	2	0.0

224	durable agriculture irrigation machine/farm irrigation system/sprinkler irrigation	1	1	103	1		0	4.7	3.0	4.8	4.6	1	1	1	1	1350.0	1690.0	yucheng yili machinery co., ltd.	unverified	1	chine	12	4.5

225	agricultural gasoline engine cultivator agricultural machinery	1	1	187	1		0	4.8	24.0	4.7	4.6	1	1	1	1	835.0	875.0	qingdao test new materials co., ltd.	unverified	1	chine	4	4.6

226	agricultural machinery /west africa power tiller hot sale pricegasoline generator	1	1	188	1		0	5.0	1.0	5.0	5.0	1	1	1	1	450.0	490.0	guangzhou yiqihang trading co., ltd	unverified	1	chine	1	4.8

227	china tractors 4wd farm tractor price agricultural machinery	1	1	165	1		10	4.3	8.0	4.5	4.6	1	1	1	1	1200.0	2300.0	dongguan dida machinery co., ltd.	unverified	1	chine	1	4.2

228	f500 electric agricultural machinery chaff cutter / straw chopper machine/corn silage chopper for sale	1	5	190	1		0	0.0	0.0	0.0	0.0	1	1	1	1	230.0	230.0	holding dcs	unverified	2	france	1	0.0

229	electric backpack agricultural machine 20l	1	2	191	1		90	0.0	0.0	0.0	0.0	1	1	1	1	44.8	44.8	shandong ucarry machinery co., ltd.	unverified	5	chine	5	4.9

230	best price agriculture machine for rice and wheat harvester binder	1	1	192	1		0	5.0	2.0	4.6	4.5	1	1	1	1	3000.0	3500.0	henan tongchen machinery equipment co., ltd	unverified	0	chine	1	0.0

231	farm tractors agricultural machinery & equipment for farm used tractor	1	1	195	1		0	0.0	0.0	0.0	0.0	1	1	1	1	11050.0	11050.0	yucheng agri machinery co., ltd.	unverified	1	chine	8	4.8

232	new type of agricultural machinery with plow for ditching and weeding four-wheel drive rotary tiller and soil loosening machine	1	1	196	1		0	0.0	0.0	0.0	0.0	1	1	1	1	438.0	526.0	zhengzhou yingju network technology co., ltd.	unverified	1	chine	3	3.1

233	gasoline agricultural machinery 4.2kw farm equipment/mini rotary tiller, high quality agricultural machinery	1	1	197	1		0	4.8	3.0	4.9	5.0	1	1	1	1	292.0	405.0	shandong qufu taifeng mechanical equipment co., ltd.	unverified	2	chine	3	4.5

234	ht105fb 9hp gasoline multipurpose korea agricultural machinery	1	1	198	1		0	0.0	0.0	0.0	0.0	1	1	1	1	275.0	290.0	liftsun machinery	unverified	2	malaisie	1	0.0

235	china farm equipment small agriculture machinery	1	5	199	1		0	5.0	2.0	5.0	5.0	1	1	1	1	260.0	360.0	e.g trading	unverified	2	france	1	0.0

236	agriculture machinery automatic loading bagging dry wet dual-purpose tractor driven peanut groundnut picker harvester machine	1	1	200	1		0	4.6	40.0	4.7	4.7	1	1	1	1	1500.0	2490.0	henan vonong machinery co., ltd.	unverified	0	chine	1	0.0

237	cambodia ploughs machine motorized hoe agricultural machinery farm equipment	1	100	118	1		0	5.0	11.0	5.0	5.0	1	1	1	1	149.0	459.0	henan xifa network technology co., ltd.	unverified	2	chine	2	4.4

238	best selling peanut harvester agriculture machine for a reasonable price	1	1	201	1		0	5.0	3.0	5.0	5.0	1	1	1	1	880.0	990.0	zhecheng hong xin machinery factory	unverified	3	chine	15	4.7

239	double track agricultural machinery micro cultivator small-land rice dry fields rotary tilling weeding trenching soil plowing	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	291.2	364.0	qufu hongbo machinery and equipment co., ltd.	unverified	2	chine	2	5.0

240	high standard massey ferguson tractor 290 agricultural machinery	1	2	202	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	2000.0	laizhou kaixiang machinery co., ltd.	unverified	0	chine	1	0.0

241	tractor plough point for agricultural machines	1	2000	203	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1.5	1.6	jining haohong industrial and mining equipment co., ltd.	unverified	3	chine	9	4.3

242	60hp 4wd farm tractor with front loader disc lawn mower backhoe used farm agricultural machine	1	1	152	1		4	4.5	12.0	4.4	4.5	1	1	1	1	2000.0	5000.0	yiwu xinchen power tools co., ltd.	unverified	0	chine	1	0.0

243	hand held agricultural machinery mini crawler cultivator farm ploughing machine rotary power tiller	1	1	99	1		5	4.9	41.0	4.9	4.9	1	1	1	1	100.0	200.0	nanning avian agricultural machinery co., ltd.	unverified	1	chine	7	4.9

244	oem manufacturers electric manual agricultural sprayers agriculture machinery equipment	1	1	204	1		0	3.4	4.0	3.8	4.0	1	1	1	1	15.6	17.5	zhejiang ting neng sheng machine co., ltd.	unverified	0	chine	19	0.0

245	combine harvester agriculture machinery for rice and wheat cheap combine harvester	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	4500.0	sichuan xudong machinery manufacture co., ltd.	unverified	0	chine	7	4.8

246	used tractor holland fiat 110-90 130-90 160-90 180-90 farm orchard compact tractor agricultural machinery 6 cylinders	1	1	150	1		0	5.0	1.0	5.0	5.0	1	1	1	1	9000.0	11000.0	henan hongen machinery equipment co., ltd.	unverified	1	chine	1	4.6

247	kat 3004-a1 agricultural tractor other agricultural machinery & equipments agriculture equipment and tools chinese tractors	1	1	205	1		0	0.0	0.0	0.0	0.0	1	1	1	1	75000.0	100000.0	xinxiang toenter technology development co., ltd.	unverified	1	chine	7	4.4

248	used agricultural machinery & equipment/farm tractor	1	700	206	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4459.2	6688.8	weifang shixin zhongkai trade co., ltd.	unverified	1	chine	3	5.0

249	fairly used agriculture machinery combine harvester for rice and wheat cheap combine harvester	1	1	121	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0	shandong tourbillon machinery co., ltd.	unverified	0	chine	2	0.0

250	agriculture machinery 4 row rice transplanter china kubota nspu-68c high speed rice planting machine 4 & 6 6 and 8 rows 6 filas	1	5	207	1		0	3.6	3.0	3.8	3.6	1	1	1	1	1500.0	2000.0	shandong sunway machinery co., ltd.	unverified	2	chine	2	5.0

251	agricultural machinery 24 disc harrow and factory prices are booming	1	1	208	1		0	4.5	8.0	4.7	4.8	1	1	1	1	977.0	1115.0	shandong nuoman engineering machinery co., ltd.	unverified	5	chine	7	4.6

252	tractors mini 4x4 farming machine agricultural/farm machinery equipment	1	1	129	1		2	1.0	1.0	1.0	1.0	1	1	1	1	4000.0	5000.0	shaanxi shengshi jiaoyang import export co., ltd.	unverified	1	chine	2	4.3

253	massey ferguson 390 agricultural machinery / fairly used 100hp mf390 farm tractor available for sale	1	1	209	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	1500.0	hebei shuoxin machinery manufacturing co., ltd.	unverified	1	chine	7	4.3

254	agricultural machinery air-suction precision seeder machine for sale	1	2	210	1		0	4.8	6.0	4.6	4.3	1	1	1	1	10500.0	10500.0	shanghai shingmore bridge imports & exports co., ltd.	unverified	0	chine	14	5.0

255	agriculture machinery 4feet tractor blade box scraper box grader land leveler	1	1	211	1		48	0.0	0.0	0.0	0.0	1	1	1	1	260.0	270.0	chongqing meiqi industry co., ltd.	unverified	0	chine	13	5.0

256	hot sale agricultural machinery boom sprayer tractor pto driven hydraulic arm spread type spray machine	1	1	157	1		58	5.0	2.0	5.0	5.0	1	1	1	1	560.0	630.0	henan wisely machinery equipment co., ltd.	unverified	1	chine	8	4.3

257	farm tools agriculture machine made in china soil preparation machine farm cultivator gasoline multi task	1	1	212	1		0	4.5	2.0	4.8	5.0	1	1	1	1	280.0	315.0	jinan minglun machinery co., ltd.	unverified	1	chine	7	5.0

258	agricultural machinery farming soil hand small ploughing machine	1	1	124	1		0	5.0	6.0	5.0	5.0	1	1	1	1	500.0	1500.0	zhengzhou rongchang machinery manufacturing co., ltd.	unverified	0	chine	1	0.0

259	sugarcane seedling planting machine for agricultural machinery fertilization and drip irrigation seeding machine manufacturer	1	1	213	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2600.0	2800.0	harbin dadi biology organic fertilizer co., ltd.	unverified	0	chine	14	0.0

260	agricultural machinery sugarcane harvester loader sugarcane cutting machine wheeled sugar cane machine	1	1	214	1		0	0.0	0.0	0.0	0.0	1	1	1	1	75000.0	80000.0	qingdao sunever machinery parts co., ltd.	unverified	1	chine	7	5.0

261	new tractor rotavator agricultural machinery tiller rotary cultivator	1	1	107	1		0	4.8	8.0	4.7	4.5	1	1	1	1	570.0	620.0	weifang jialinuo agriculture machinery equipment co., ltd.	unverified	1	chine	6	4.5

262	high quality manual battery 16l knapsack sprayer agriculture machine/agriculture spray	1	50	215	1		86	4.9	35.0	4.9	4.8	1	1	1	1	16.0	30.0	soc etablissements vezin	unverified	2	france	1	0.0

263	mechanical seeder agricultural machinery e vegetable seeds planting machine seeders transplanters home use sembradora de maiz	1	5	128	1		4	4.7	37.0	4.7	4.7	1	1	1	1	42.0	44.9	zhejiang leming industry and trading company ltd.	unverified	0	chine	1	5.0

264	shandong new 40hp mini tractor agricultural machinery with great price and high durability	1	1	131	1		0	5.0	17.0	5.0	5.0	1	1	1	1	4400.0	4500.0	shandong yuanchuan machinery co., ltd.	unverified	1	chine	3	4.5

265	agricultural machinery tool a farm pit digger used with a tractor hole digger	1	20	107	1		0	4.8	8.0	4.7	4.5	1	1	1	1	392.0	400.0	nanchang edward technology co., ltd.	unverified	4	chine	12	4.8

266	backbone machinery 5in1 mini rice mill machine rice millet corn milling flour milling machine	1	1	159	1		4	4.8	19.0	4.7	4.7	1	1	1	1	350.0	380.0	xi'an meishi jinlin import and export co., ltd.	unverified	0	chine	4	4.7

267	radish vegetable planter machine clover manual corn bean seeder seed planting machines seeder machine farmland plain lands	1	1	128	1		0	4.7	37.0	4.7	4.7	1	1	1	1	42.0	45.0	taian mingyi machinery equipment co., ltd.	unverified	3	chine	5	5.0

268	40 hp agriculture farming mini compact yto tractor price with front end loader	1	1	19	1		0	4.8	9.0	4.7	4.6	1	1	1	1	4000.0	4000.0	dongguan city strong machinery equipment co.,lt,d	unverified	0	chine	1	0.0

269	cheap 30hp 40hp 50hp 60hp mini wheeled agricultural tractor 120 power 4x4 agriculture tractor loader for sell	1	1	96	1		0	4.4	108.0	4.4	4.3	1	1	1	1	988.0	988.0	sayginlar tarim makinalari otomotiv insaat malzemeleri gida sanayi ve ticaret limited sirketi	unverified	0	turquie	8	0.0

270	farm equipment pneumatic air suction precision 2 4 6 8 10 rows maize corn planter seeder machine tractor mounted price for sale	1	1	132	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8700.0	8900.0	linyi gama machinery co., ltd.	unverified	0	chine	2	5.0

271	anon 5 row self-propelled agricultural machine cotton picker	1	1	114	1		0	5.0	5.0	4.7	4.2	1	1	1	1	308800.0	312000.0	eastman industries limited	unverified	2	inde	13	0.0

272	kubota tractors m954kq 95hp farm a small agricultural tractor used in orchards tractors	1	1	162	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	4500.0	wadani wholesale kg	unverified	1	autriche	2	0.0

273	used mf 385 mf 390 4x4 tractor agricultural machinery massey ferguson tractor farm tractors for sale france	1	1	163	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3220.0	3220.0	sarolta sarolta handels gmbh	unverified	2	autriche	1	0.0

274	farm tractors gearbox agricultural machinery equipment rice mill 2100 hot sales chinese manufacturer 50hp 60hp 70hp 2wd 4wd	1	1	125	1		4	4.3	5.0	4.5	5.0	1	1	1	1	5900.0	6300.0	pinoyweb tljcom trading	unverified	0	philippines	7	0.0

275	original quality fairly used new hollands 70hp 4wd agricultural farm tractor with free disc harrow	1	1	164	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	4000.0	laizhou lida machinery co., ltd.	unverified	3	chine	2	5.0

276	china in hydraulic earth auger earth auger drilling machine earth auger with hand rack	1	1	47	1		1	4.4	13.0	4.3	4.3	1	1	1	1	620.0	640.0	farmburg agro	unverified	2	inde	7	0.0

277	agricultural machinery equipment diesel cultivator motocultor two wheel gasoline power mini tiller 18 hp walking tractor	1	1	165	1		2	4.3	8.0	4.5	4.6	1	1	1	1	480.0	480.0	shandong dongcheng machinery manufacturing co., ltd.	unverified	4	chine	2	3.5

278	cheep agricultural equipment hydraulic reversible turning plough machine share plow for tractor	1	1	168	1	CE	0	4.5	125.0	4.4	4.3	1	1	1	1	880.0	880.0	shenyang vhandy technology co., ltd.	unverified	1	chine	8	5.0

279	agricultural big center pivot irrigation machine solar center pivot irrigation system for sale	1	1	79	1		0	3.3	4.0	3.8	4.2	1	1	1	1	15000.0	50000.0	qingzhou aike machinery technology co., ltd.	unverified	0	chine	8	0.0

280	agricultural machinery mini tractor 4*4 35hp tractor price for small farm	1	1	172	1		0	3.6	2.0	4.0	4.5	1	1	1	1	1180.0	1230.0	yancheng xinmingyue machinery manufacture co., ltd.	unverified	0	chine	6	0.0

281	small plough machine cultivator gasoline and diesel engine mini self propelled power tiller rotary cultivator	1	1	161	1		0	3.6	2.0	3.2	3.0	1	1	1	1	260.0	300.0	shandong react machinery co., ltd.	unverified	3	chine	4	4.9

282	garden manual hand ploughing walking tractor agricultural maquinas agricolas	1	1	118	1		0	5.0	11.0	5.0	5.0	1	1	1	1	149.0	459.0	taizhou sansheng machinery co., ltd.	unverified	0	chine	3	5.0

283	chalion agricultural wheat seeder machine farm wheat seeder price 12 row farm wheat seed planter for tractor	1	3	13	1		1	5.0	8.0	5.0	5.0	1	1	1	1	5499.0	5499.0	shandong yihe agricultural technology co., ltd.	unverified	0	chine	1	5.0

284	small agricultural tractor 90hp chinese tractor 4x4 farm good quality machine tractor	1	1	160	1		0	4.8	3.0	4.7	4.6	1	1	1	1	8005.0	8005.0	solution beta	unverified	3	danemark	2	0.0

285	tractor agricultural machinery massey ferguson can choose epa engine tractor farm used tractors for sale	1	1	15	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2050.0	2550.0	henan strosen industry co., ltd.	unverified	2	chine	5	4.7

286	buy cheap original fairly used farm agricultural machinery combine harvester with 14 foot header for sale	1	1	216	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	5000.0	henan amk group	unverified	1	chine	7	4.4

287	cheap fairly used mf 6280 agricultural tractor for sale	1	10	217	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	4500.0	zhengzhou xuchen agricultural machinery co., ltd.	unverified	1	chine	1	0.0

288	land universal four-wheel drive 50hp agricultural field cultivator tractor wheel farm traktor 4wd tractor price for sale	1	1	218	1		0	5.0	4.0	5.0	5.0	1	1	1	1	2000.0	2100.0	dongguan city strong machinery device co., ltd.	unverified	0	chine	1	0.0

289	agricultural machinery farm hoe mini power tillers rotary cultivator	1	1	166	1		0	4.2	16.0	4.2	4.1	1	1	1	1	360.0	360.0	shenzhen strong machinery equipment co.,ltd.	unverified	0	chine	1	0.0

290	quality used new hollland snh904 agricultural tractors in second hand farm with loader	1	1	219	1		0	4.6	14.0	4.5	4.7	1	1	1	1	3960.0	5960.0	newindu construction engineering (shanghai) co., ltd.	unverified	5	chine	8	5.0

291	cheap 12hp 15hp 18hp tractor 7-200 power agriculture tractors 4x4 farm tractor for sale with auxiliary equipment	1	1	220	1		0	5.0	1.0	5.0	5.0	1	1	1	1	5120.0	5623.0	luohe juyou commercial & trading co., ltd.	unverified	4	chine	9	4.6

292	wheel sprayer agriculture products spraying machines orchard sprayer agricultural	1	1	221	1		0	0.0	0.0	0.0	0.0	1	1	1	1	990.0	1090.0	shanghai kaiertan machinery co., ltd.	unverified	2	chine	2	4.6

293	hay cutter flail mower tractor other farm machines tractors new tractors for agriculture in korea	1	1	222	1		3	5.0	5.0	5.0	5.0	1	1	1	1	3000.0	5000.0	yantai chengfeng machinery technology co., ltd.	unverified	3	chine	3	4.6

294	subsoiler standard subsoiler agricultural machinery farm cultivator hot sale subsoiler deep loosening soil machine	1	1	29	1		0	4.9	10.0	4.9	4.9	1	1	1	1	1500.0	2500.0	shandong luyu international trade co. ltd	unverified	3	chine	3	5.0

295	fairly used massey ferguson 135 2wd agricultural machinery	1	1	209	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	1500.0	danyang tianda intelligent technology co., ltd.	unverified	2	chine	4	5.0

296	95hp 4wd john & deere 5e954 used tractor agricultural machinery & equipment for farm	1	8	223	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9999.0	9999.0	sarl se des ets boudon	unverified	2	france	1	0.0

297	hotoka 63cc power tiller&cultivator small ploughing agricultural machine farm soil motor tiller mini tractor rotary tiller price	1	2	20	1	CE	2	4.8	40.0	4.9	4.9	1	1	1	1	68.0	80.0	yucheng zeyi machinery co., ltd.	unverified	1	chine	8	4.8

298	kubota 7171 tractor agricultural machinery & equipment	1	1	26	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	shenzhen strong machinery co.,ltd.	unverified	0	chine	1	0.0

299	zzgd 170/177/188 diesel agricultural machinery farm hoe mini power tillers rotary cultivator	1	1	149	1		0	3.8	58.0	3.7	3.6	1	1	1	1	250.0	628.0	yantai lutian commercial co., ltd.	unverified	0	chine	1	0.0

300	2023 high quality bulk importer sub soilers farm use agriculture machine for buy at lowest price	1	1	123	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1155.0	1550.0	xi'an huan yu jingjie trading co., ltd.	unverified	1	chine	4	4.4

301	multifunction power tiller agricultural machinery deep cultivating power tiller blade agriculture machine	1	1	98	1		0	5.0	3.0	5.0	5.0	1	1	1	1	650.0	650.0	xingtai tingyang machinery equipment co., ltd.	unverified	1	chine	1	0.0

302	chinese hot sale agricultural machinery 5.5hp high efficiency rotary mini power tiller hand push cultivator for farming land	1	1	212	1		0	4.5	2.0	4.8	5.0	1	1	1	1	280.0	315.0	shandong hongqi machinery & electric group co., ltd.	unverified	0	chine	10	0.0

303	4/6m hydraulic folding compacting suppression roller agricultural machinery	1	1	224	1		0	4.5	2.0	4.5	4.5	1	1	1	1	2100.0	2500.0	henan qinbiao industrial development co., ltd.	unverified	2	chine	2	4.4

304	agricultural machinery and equipment specialized for wheat sowing tractor equipment wheat seeder	1	1	103	1		0	4.7	3.0	4.8	4.6	1	1	1	1	750.0	1550.0	henan new yongyuan machinery equipment co., ltd.	unverified	0	chine	1	0.0

305	1.25m width tiller cultivators agricultural machine price	1	1	18	1	CE	0	4.5	14.0	4.5	4.5	1	1	1	1	315.0	340.0	changzhou maikey machinery equipment co., ltd.	unverified	0	chine	4	4.7

306	used deutz fahr tractors 100hp 4x4wd agricultural machinery & equipment compact tractor with front end loader	1	1	120	1		0	4.8	36.0	4.8	4.7	1	1	1	1	6000.0	6000.0	shandong rippa machinery group co., ltd.	unverified	5	chine	5	4.6

307	chinese hot selling 5hp high efficiency agricultural machinery plastic mulch laying machine for orchard garden	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	480.0	510.0	shenzhen city strong machinery co., ltd.	unverified	0	chine	1	5.0

308	new design tracteur traktor blue color 50hp 55hp 4 wheel farm small tractor agricultural machinery with attachment	1	1	152	1		5	4.5	12.0	4.4	4.5	1	1	1	1	4500.0	5980.0	maxizm construction machinery (qingdao) co., ltd.	unverified	4	chine	5	5.0

309	used new rice transplanter kubota transplanters agricultural equipment machinery 6 rows 8 rows for sale	1	1	150	1		0	5.0	1.0	5.0	5.0	1	1	1	1	6000.0	8000.0	shandong msang machinery co.,ltd.	unverified	4	chine	4	4.6

310	massey ferguson agricultural machinery / used 85hp farm tractor	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	shandong creations machinery co., ltd.	unverified	1	chine	8	4.2

311	agriculture machinery hand push corn planter maize seeder hand wheat planter	1	1	211	1		0	0.0	0.0	0.0	0.0	1	1	1	1	80.0	85.0	shandong feichuang machinery manufacturing co., ltd.	unverified	3	chine	4	4.4

312	monorail small walking tractor agricultural machinery farm equipment mountain slopes plowing machine gasoline/diesel cultivator	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	201.6	252.0	henan jinfuda trading co., ltd.	unverified	3	chine	4	4.5

313	original quality agriculture machinery combine harvester for rice and wheat cheap combine harvester available in france	1	1	155	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	7000.0	ash gmbh & co. kg	unverified	2	allemagne	2	0.0

314	agriculture machinery farm tilling cultivator tractor light duty rotary tiller	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	452.0	452.0	henan yibao machinery equipment co., ltd.	unverified	3	chine	6	4.4

315	compact farm tractor agricultural machine 25hp 30hp 35hp 40hp 45hp	1	1	156	1		0	5.0	2.0	5.0	5.0	1	1	1	1	2799.0	2899.0	j blue tokyo co., ltd.	unverified	2	tha�lande	3	0.0

316	used japan professional rice planter small agricultural machine	1	1	36	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	15000.0	marcello food & beverages	unverified	2	france	2	0.0

317	new design tractor mounted semi-automatic tree planter planting machine for olive tree	1	1	153	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8300.0	8600.0	henan zlin heavy industry group co., ltd.	unverified	5	chine	2	5.0

318	factory price high productivity easy to operate peanut shelling machine peanut skin peeling machine	1	1	109	1		24	4.1	40.0	4.2	4.3	1	1	1	1	118.0	138.0	yiwu hangyuan machinery equipment co., ltd.	verified	0	chine	1	4.5

319	tingxiang rice mini wheat thresher diesel engine small threshing machine grain soybeans paddy thresher rice thresher machine	1	1	33	1		0	5.0	7.0	5.0	5.0	1	1	1	1	115.0	120.0	shandong hanwo agricultural equipment co., ltd.	unverified	0	chine	1	0.0

320	seeder onion planting machine transplanters hand manual corn seeder machine planter corn planter planting machine	1	2	158	1		0	5.0	2.0	5.0	5.0	1	1	1	1	59.0	59.0	yiwu lingang machinery equipment co., ltd.	unverified	0	chine	1	0.0

321	high quality multifunctional rice thresher machine maize corn threshing machine on sale	1	1	157	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1000.0	1100.0	zhengzhou caleb machinery co., ltd.	unverified	2	chine	3	4.3

322	15hp- 200hp tractor universal tractor china agricultural machinery tractor	1	1	19	1		0	4.8	9.0	4.7	4.6	1	1	1	1	28000.0	28000.0	anyang aols machinery equipments co., ltd.	unverified	2	chine	8	4.1

323	ifourni 15l knapsack 2 stroke power manual sprayer tu-26 agriculture sprayers	1	1	128	1		2	4.7	37.0	4.7	4.7	1	1	1	1	46.8	56.2	etal- fruits	unverified	2	france	2	0.0

324	backbone machinery agricultural use silage forage chopper animals feed fodder cutting chaff cutter machine machine grass chopper	1	1	159	1		58	4.8	19.0	4.7	4.7	1	1	1	1	115.0	200.0	zhengzhou guoyi baifen trading co., ltd.	unverified	1	chine	2	3.0

325	multi functional gasoline weeder loosening soil ditching and micro tillage machine corn orchard	1	1	14	1	CE	0	4.8	124.0	4.7	4.7	1	1	1	1	120.0	320.0	changzhou lefa industry & trade co., ltd.	unverified	2	chine	17	5.0

326	used second new tractor new holland shn554 55hp farm agricultural tractor	1	1	162	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	5000.0	zhumadian lovol kubota agricultural machinery sales co., ltd.	unverified	0	chine	1	0.0

327	cabin agricultural tractors with implements and loader epa 4wd 75hp farming tractor	1	1	119	1		1	4.8	12.0	4.8	4.8	1	1	1	1	5200.0	5800.0	anhui legend agricultural machinery manufacturing co., ltd.	unverified	0	chine	1	0.0

328	farm machine mini power tractor skid steer garden grass rotary tiller cultivator for sale	1	1	107	1		1	4.8	8.0	4.7	4.5	1	1	1	1	400.0	800.0	dezhou hongyou agricultural machinery co., ltd.	unverified	0	chine	1	0.0

329	anon 300m 400m farm irrigation sprinkler farm drip irrigation systems agricultural irrigation system	1	1	114	1		0	5.0	5.0	4.7	4.2	1	1	1	1	8000.0	10000.0	zhejiang teammax tool manufacture co., ltd.	verified	3	chine	14	4.7

330	good working condition mini tractor pto hay round baler straw baler machine grass round baler for sale cheap price austria	1	1	163	1		0	0.0	0.0	0.0	0.0	1	1	1	1	850.0	850.0	shenzhen yishitong technology co., ltd.	verified	1	chine	3	4.5

331	agriculture 3 point tractor potato subsoiler ripper plough	1	1	132	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	10000.0	henan silk road machinery co., ltd.	unverified	1	chine	9	3.6

332	agricultural machinery small mini 4x4 compact farm tractor.	1	1	165	1		0	4.3	8.0	4.5	4.6	1	1	1	1	1300.0	2500.0	yongkang huawei machinery co., ltd.	unverified	0	chine	6	4.2

333	best factory 4x4 new 50hp jd 1026r agriculture machinery equipment farm tractors available now on stock	1	1	164	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2600.0	yancheng foreign machinery parts co., ltd.	unverified	0	chine	16	0.0

334	agricultural soil preparation machinery disc harrow harro1bz-2.5 heavy disc power harrow supplier traction harrow	1	1	79	1	CE	0	3.3	4.0	3.8	4.2	1	1	1	1	2200.0	2600.0	taizhou city chunfeng machinery co., ltd.	unverified	1	chine	6	5.0

335	best price farm machine hand walking tractor 8hp hand orchard garden lawn walking tractor two wheel walking tractor changfa	1	1	118	1		0	5.0	11.0	5.0	5.0	1	1	1	1	396.0	456.0	qingdao shengshide machinery co., ltd.	unverified	1	chine	8	3.0

336	land universal free shipping mini tractor 4x4 for farming agriculture hydraulic tractor 50hp	1	1	218	1		0	5.0	4.0	5.0	5.0	1	1	1	1	2000.0	2100.0	taizhou jialong baofeng agriculture machinery co., ltd.	unverified	1	chine	9	0.0

337	purchase quality massey ferguson 4x4 100hp/120hp agricultural machinery used farm tractor available in stock with free shipment	1	1	216	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2100.0	3500.0	henan elorry industrial co., ltd.	unverified	5	chine	2	4.4

338	gasoline engine diesel engine mini plough small tiller machine china factory direct sell	1	1	161	1		0	3.6	2.0	3.2	3.0	1	1	1	1	260.0	300.0	qingzhou shangxin power machinery co., ltd.	unverified	1	chine	5	4.5

339	smail agricultural machinery cultivator 3-point power rotary blades tiller gearbox for farm tractor motoculteur tiller rotary	1	1	220	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1100.0	1180.0	eagle power machinery (jingshan) co., limited	unverified	1	chine	3	5.0

340	original mf 385 mf 390 4x4 tractor agricultural machinery massey fergusson gc1715 tractor farm tractors for sale	1	10	217	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	3500.0	qingdao wander international trade co., ltd.	unverified	0	chine	3	0.0

341	agricultural machinery maize harvesting machine small harvest machine mini pea bean soybean wheat rice combine harvester	1	1	166	1		0	4.2	16.0	4.2	4.1	1	1	1	1	4800.0	4800.0	changzhou kavan machinery co., ltd.	unverified	0	chine	6	5.0

342	three spray modes three in one nozzle sprayer for farm agriculture machine sprayers	1	1	221	1		4	0.0	0.0	0.0	0.0	1	1	1	1	8.0	10.0	shandong jintop machinery co., ltd.	unverified	2	chine	3	5.0

343	25 ps mini tractor mini 4x4 25hp epa ce 25hp machinery multifunction mini tractor	1	1	222	1		3	5.0	5.0	5.0	5.0	1	1	1	1	3000.0	4000.0	weifang cp machinery co., ltd.	unverified	0	chine	11	5.0

344	quality original case ih agricultural machinery tractors available for sale	1	1	48	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2787.0	3344.4	luohe tengao mechanical and electrical equipment co., ltd.	unverified	2	chine	5	4.7

345	fairly used mf7720 agricultural machinery / massey ferguson 7720 180hp tractor for sale	1	1	209	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	4000.0	nanyang xinda electro-mechanical co., ltd.	unverified	1	chine	11	4.8

346	new lovol f411o tractor farm mini tractor garden agriculture machinery	1	1	26	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0	general ingredients	unverified	2	france	1	0.0

347	agricultural machinery,precision wheat seeder seed drill 14 rows no-tillage seeding and fertilizing precision wheat sower	1	1	29	1		0	4.9	10.0	4.9	4.9	1	1	1	1	555.0	578.0	yucheng dadi machinery co., ltd.	unverified	0	chine	16	0.0

348	new arrival brand new and john used deere 85hp 95hp 120hp 140hp farm tractor agricultural machinery & equipment	1	3	223	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9999.0	9999.0	ningbo aosheng machine co., ltd.	unverified	2	chine	16	0.0

349	cultivators diesel power tiller agricultural machinery and equipment ruris tiller farm cultivator	1	1	98	1		0	5.0	3.0	5.0	5.0	1	1	1	1	650.0	650.0	shandong tongrun import and export co., ltd.	unverified	2	chine	2	4.6

350	chinese popular agricultural machinery 5.5hp hand rotary mini power tiller orchard farm garden cultivator	1	1	212	1		0	4.5	2.0	4.8	5.0	1	1	1	1	300.0	320.0	sarl eta cardiet	unverified	2	france	2	0.0

351	automatic retraction irrigation pipe used agricultural machine	1	1	103	1		0	4.7	3.0	4.8	4.6	1	1	1	1	1070.0	1396.0	jinan zongmao import & export co., ltd.	unverified	0	chine	2	0.0

352	high efficiency agricultural machinery 5hp gasoline power orchard garden farm plastic mulch laying machine	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	480.0	510.0	jining toho machinery co., ltd.	unverified	4	chine	4	5.0

353	used/second hand/new wheel tractors 4x4wd johnn deer 5e 1004 100hp with small compact farm equipment agricultural machinery	1	1	120	1		0	4.8	36.0	4.8	4.7	1	1	1	1	8965.0	8965.0	shandong cnmc machinery co., ltd.	unverified	5	chine	6	4.7

354	deutz fahr 5080 d tractor keyline - front loader agricultural machinery & equipment	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	3500.0	shandong eachan machinery group co., ltd.	unverified	3	chine	4	4.8

355	multifunctional horse-capable double track cultivator powerful rotary tillage furrowing dry paddy fields agricultural machinery	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	309.4	364.0	nanje enterprises	unverified	2	afrique du sud	3	0.0

356	agricultural machinery is an efficient rotary tiller that can be used on a family farm. to meet market demand	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	452.0	452.0	kefer invest gmbh	unverified	2	allemagne	3	0.0

357	largest farm agriculture machine small products made in japan	1	1	36	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	15000.0	chongyuan machinery ltd	unverified	1	�tats-unis	1	0.0

358	chinese agricultural machinery yituo yto 454 farm tractor	1	3	41	1		0	5.0	11.0	4.9	4.9	1	1	1	1	9300.0	9300.0	oriemac machinery & equipment (shanghai) co., ltd.	unverified	3	chine	8	5.0

359	wholesale agriculture machinery equipment diesel power tiller cultivators agricultural farm machine crawler rubber track tractor	1	1	225	1		0	4.7	28.0	4.6	4.4	1	1	1	1	6375.0	6375.0	cruking engineering equipment (xiamen) co., ltd.	unverified	4	chine	4	5.0

360	austria cheap 4wd 4x4 30hp 50hp 80hp 120hp mini farm tractors used kubota agriculture farm machinery cheap farm tractor	1	1	108	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2155.0	2755.0	linyi shunkai international trade co., ltd.	unverified	1	chine	15	5.0

361	cheap kubota 4x4 tractor for agriculture m704k tractor farm machine lawn mowing tractor	1	1	145	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1114.8	2229.6	taizhou chagesi machinery co., ltd.	unverified	0	chine	2	0.0

362	joyance drones agricultural machine power crop farm sprayer oil electric hybrid drone sprayer	1	1	76	1	CE	2	5.0	20.0	5.0	5.0	1	1	1	1	8000.0	9800.0	hangzhou joins import and export co., ltd.	unverified	2	chine	10	4.7

363	used tractor agricultural machinery massey ferguson 174 tractor farm tractors for sale	1	10	217	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	3500.0	chongqing ailinyou technology co., ltd.	unverified	1	chine	4	5.0

364	small agricultural multifunctional gasoline rototiller cultivators agricultural manual tillers	1	1	226	1		0	5.0	5.0	4.8	4.8	1	1	1	1	115.0	117.0	dalian huaxing yulin technology co., ltd.	unverified	0	chine	3	0.0

365	agricultural highefficiency dry and wet dualpurpose corn straw crusher for cattle and sheep feed crushing and cutting grass	1	1	227	1		1	4.1	18.0	4.2	4.2	1	1	1	1	259.0	259.0	taizhou kesiwo garden tools co, ltd.	unverified	0	chine	1	5.0

366	top selling foton lovol tractor 50hp 4wd 30hp 80hp 120hp mini farm tractor 4x4 agriculture farm machinery cheap farm tractor	1	1	228	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1800.0	1800.0	qingdao haoge yunzhi technology co., ltd.	unverified	1	chine	2	5.0

367	mini walking 100hp tractor agricultural machinery equipment diesel engine 4 wheel tractors	1	1	229	1	CE	0	4.9	23.0	4.9	4.8	1	1	1	1	6300.0	7000.0	shandong jierui machinery equipment co., ltd.	unverified	3	chine	3	4.5

368	latest design reed straw grass harvesting and bundling machine cattail oat corn stalk harvester binder diesel engine	1	1	75	1		0	5.0	17.0	5.0	5.0	1	1	1	1	2200.0	3900.0	shijiazhuang sanli grain sorting machinery co., ltd.	unverified	1	chine	16	5.0

369	agricultural square baler heavy duty large square hay balers	1	1	170	1		0	4.8	6.0	4.6	4.6	1	1	1	1	5500.0	5900.0	nanchang huibing electronics co., ltd.	unverified	2	chine	6	4.7

370	handheld lawn mowers, agricultural machinery, small gasoline lawn mowers, gardening tools, lawn mowers	1	1	230	1		0	0.0	0.0	0.0	0.0	1	1	1	1	100.0	120.0	zhejiang mingjia environmental protection technology co., ltd.	unverified	0	chine	7	0.0

371	high quality professional 52cc 2.2hp cultivator mini agriculture equipment and tools,power tiller,easy start farming equipment	1	1	117	1		0	0.0	0.0	0.0	0.0	1	1	1	1	75.0	100.0	yiwu kewen machinery equipment co., ltd	unverified	0	chine	1	3.0

372	agricultural tools machinery avoidance lawn mower avoid tree weeder orchard woods	1	1	231	1		0	4.8	6.0	4.8	4.8	1	1	1	1	1320.0	1360.0	shandong changmei machinery equipment co., ltd	unverified	1	chine	4	4.5

373	high quality agricultural machinery use mini power tillers 8hp rotary cultivator for farm and home 50 multifunctional provided	1	1	232	1		0	3.1	8.0	3.2	3.3	1	1	1	1	347.0	410.0	wuhan wubota machinery co., ltd.	unverified	1	chine	6	5.0

374	walking tractor with plough / tiller /grass mower 18hp hand walking agricultural tractor	1	1	233	1		0	4.2	19.0	4.4	4.5	1	1	1	1	480.0	500.0	zhejiang e-shine machinery technology co., ltd.	unverified	0	chine	7	5.0

375	china cheap price farm tractor 30hp 40hp 50hp 60hp 70hp 80hp 90hp 4wd machinery agriculture tractor spare parts	1	1	234	1		0	0.0	0.0	0.0	0.0	1	1	1	1	999.0	7888.0	shenzhen wishope technology co., ltd.	unverified	0	chine	16	0.0

376	best supplier of original fairly used massey ferguson tractors , massey ferguson 175 agricultural tractors	1	2	235	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2600.0	2600.0	anhui chunfeng nonglin machinery manufacturing co., ltd.	unverified	0	chine	4	5.0

377	import tractor agriculture machine mini 4x4 farming best chinese tractor with front end loader 50hp 200hp cheap farm tractors	1	1	236	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3999.0	9999.0	yongkang united mechanic co., ltd.	unverified	1	chine	7	4.8

378	agricultural chain roller trolley machine self-propelled diesel plow machine single wheel chain rail tiller engine provided 80	1	1	237	1		0	4.4	15.0	4.4	4.4	1	1	1	1	350.0	399.0	chongqing dazu minzhili hardware manufacturing co., ltd.	unverified	1	chine	5	4.6

379	agricultural machinery harvester groundnut picking machine peanut harvesting picker	1	1	238	1		0	4.6	49.0	4.7	4.6	1	1	1	1	1999.0	3300.0	henan sinoway trading co., ltd.	unverified	2	chine	4	5.0

380	chinese gasoline 52-63cc ground hole drilling machine earth auger with 1.7-2.27kw engine gasoline ground drill	1	1	45	1		0	5.0	3.0	5.0	5.0	1	1	1	1	22.0	150.0	shandong xinleichuang machinery co., ltd.	unverified	1	chine	1	5.0

381	china taizhou jc s01 agricultural machinery manual hand planter seeder factory price	1	1	44	1		0	4.3	6.0	4.6	4.8	1	1	1	1	39.0	49.0	luoyang lutong trading co., ltd.	unverified	0	chine	4	0.0

382	agriculture machinery equipment farm 4x4 tractor farm tractor 75hp	1	1	111	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3500.0	weifang runshine machinery co., ltd.	unverified	1	chine	14	4.0

383	high quality and easy to operate factory supply 50 hp four-wheel dongfeng small agricultural tractor 4x4 mini farming tractors	1	1	239	1		0	5.0	3.0	5.0	5.0	1	1	1	1	3888.0	3888.0	henan share m&e equipment co.,ltd	unverified	2	chine	2	4.6

384	new type of small rotary tiller hoeing cultivator home garden management machine two-stroke gasoline machine agricultural tools	1	1	16	1		0	4.5	30.0	4.5	4.5	1	1	1	1	279.0	279.0	organic production	unverified	2	france	2	0.0

385	elevate farming precision with advanced crawler tractors navigate through challenging agricultural landscapes	1	1	240	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1300.0	1800.0	xuzhou chens-lift construction machinery co., ltd.	unverified	1	chine	5	5.0

386	farm equipment agriculture machine mini harvester long service life	1	1	133	1		0	5.0	2.0	5.0	5.0	1	1	1	1	260.0	310.0	deeseed inc	unverified	0	canada	1	0.0

387	high quality sports agricultural plow agricultural equipment cultivator tools	1	1	43	1		0	0.0	0.0	0.0	0.0	1	1	1	1	542.0	778.0	shandong hanyue heavy industry group co., ltd.	unverified	4	chine	3	4.4

388	farm management machine cultivator diesel rotary tiller cultivator	1	1	241	1		0	4.6	10.0	4.2	3.7	1	1	1	1	680.0	1000.0	auer trade gmbh	unverified	0	autriche	2	0.0

389	44-5 agricultural gasoline small rotary tiller, soil plow, multifunctional weeding machine, agricultural and garden tools,	1	50	242	1		0	0.0	0.0	0.0	0.0	1	1	1	1	44.1	45.2	shandong king machinery co., ltd	unverified	0	chine	2	0.0

390	high quality used tractor massey ferguson tractors mf1104 110hp agricultural machinery & equipment	1	5	223	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7000.0	7000.0	henan chuangqin mechanical equipment co., ltd.	unverified	2	chine	4	4.7

391	agricultural machinery hiller rotary tiller soil cover machine	1	1	211	1		1	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	1140.0	xinxiang rongsheng machinery co., ltd.	unverified	1	chine	2	5.0

392	hotoka 144f soil tiller cultivator agricultural machine gasoline power walking tractor mini rotary tiller for garden and farm	1	2	20	1	CE	20	4.8	40.0	4.9	4.9	1	1	1	1	95.0	125.0	shenzhen strong machinery co., ltd.	unverified	0	chine	1	0.0

393	agricultural machinery rototiller special rototiller plant sold at a low price	1	1	29	1		1	4.9	10.0	4.9	4.9	1	1	1	1	465.0	500.0	shouguang tianyu power machinery co., ltd	unverified	0	chine	1	0.0

394	75hp agricultural machinery with loader for sell / 5100m johnn deere tractor available for good price	1	1	209	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	5000.0	lincoln john intelligent equipment (shandong) co., ltd.	unverified	0	chine	2	5.0

395	farm cultivator walking tractor micro tillage machine mini agricultural machinery tiller machine	1	1	149	1		0	3.8	58.0	3.7	3.6	1	1	1	1	268.0	338.0	china vastness machinery co., ltd.	unverified	1	chine	2	4.4

396	deutz fahr 5080d keyline tractor agricultural machinery & equipment	1	1	26	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	nanjing fengdeli machinery technology co., ltd.	unverified	0	chine	4	4.5

397	3zt series spring cultivator factory direct sales agricultural machine	1	1	224	1		0	4.5	2.0	4.5	4.5	1	1	1	1	850.0	950.0	shandong dibao machinery technology co., ltd.	unverified	0	chine	4	0.0

398	multi functional ridge raising and film mulching transplanting machine seed transplanting machine for agricultural machinery	1	1	213	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3400.0	3800.0	jiangsu lihua agricultural machinery chain co., ltd.	unverified	0	chine	4	5.0

399	used tractor n holland snh804 80hp cheap farm wheel tractors 4x4wd compact agricultural equipment machinery	1	1	150	1		0	5.0	1.0	5.0	5.0	1	1	1	1	6000.0	8000.0	xingtai taiqing machinery manufacturing co., ltd.	unverified	1	chine	3	5.0

400	farm tools agricultural machinery & equipment mini tractors low price power tiller cultivators motoculteur	1	1	212	1		0	4.5	2.0	4.8	5.0	1	1	1	1	300.0	320.0	chongqing xiapu tool co., ltd.	unverified	3	chine	3	5.0

401	small cultivating machine 1gqn-125 tiller garden cultivators agricultural machinery	1	1	18	1	CE	2	4.5	14.0	4.5	4.5	1	1	1	1	340.0	370.0	qingdao rolande commercial co., ltd.	unverified	0	chine	2	5.0

402	china new multifunction agricultural machinery mini farming crawler cultivators for sale	1	1	96	1	CE	0	4.4	108.0	4.4	4.3	1	1	1	1	998.0	998.0	dandong wellgain machinery equipment co., ltd.	unverified	1	chine	4	5.0

403	purchase high accuracy kubota m9540 m8540 m7060 45-60hp tractor agricultural machine available with fast ship	1	1	22	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2300.0	2500.0	tianjin mikim technique co., ltd.	unverified	4	chine	3	4.2

404	fendt 828 tractor agricultural machines available at best price	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	hunan andewang technology co., ltd.	unverified	0	chine	2	0.0

405	tractor pto driven cultivator suppliers second agricultural machinery mini hand soil cultivating machine agricultural machinery	1	1	98	1		0	5.0	3.0	5.0	5.0	1	1	1	1	800.0	800.0	hunan dapeng machinery co., ltd.	unverified	0	chine	2	0.0

406	agricultural weeding machine gasoline weeder machine mini power weeder hot selling to nigeria	1	1	243	1		3	4.6	12.0	4.8	4.9	1	1	1	1	68.0	90.0	hunan nongfu machinery & electronic co., ltd.	unverified	0	chine	3	0.0

407	35hp mini tractor agricultural machinery suitable for a wide range of terrain	1	1	131	1		0	5.0	17.0	5.0	5.0	1	1	1	1	3400.0	3500.0	longkou longxiang mould co., ltd.	unverified	0	chine	2	0.0

408	agricultural machinery 25 hp mini remote control crawler tractor for sale	1	1	109	1		1	4.0	40.0	4.1	4.2	1	1	1	1	1600.0	1845.0	zhengzhou anho machinery co., ltd.	unverified	0	chine	2	0.0

409	popular agriculture machine selling in cambodia	1	1	244	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1100.0	1100.0	chongqing amm machinery manufacturing co., ltd.	unverified	0	chine	2	0.0

410	dawn agro mini paddy rice thresher machine threshing wheat sorghum peeling agriculture machinery in philippines	1	1	245	1		0	4.8	6.0	4.8	4.8	1	1	1	1	240.0	300.0	gookma technology industry company limited	unverified	0	chine	2	0.0

411	hot sales taifeng square grass silage straw packing machine for farm use hay baler silage bag packing baler agricultural machine	1	1	246	1		0	4.6	6.0	4.6	4.6	1	1	1	1	485.0	586.0	changsha dawning environmental protection technology co., ltd.	unverified	0	chine	3	0.0

412	low cost high quality automatic agriculture irrigation machine with 1 big rain gun sprinkler	1	1	247	1		0	4.5	12.0	4.4	4.4	1	1	1	1	950.0	1000.0	tewrex industrial machinery (suzhou) co., ltd.	unverified	0	chine	1	0.0

413	70hp agricultural tractor 4 wheel drive with ac cabin agricultural genuine tractor agriculture machinery	1	1	248	1		0	5.0	13.0	4.9	4.9	1	1	1	1	10400.0	10650.0	grwa co., limited	unverified	3	hong-kong	1	5.0

414	gasoline diesel mini plough machine small agriculture machinery with tiller	1	5	249	1		0	0.0	0.0	0.0	0.0	1	1	1	1	299.0	319.0	stav 26 corp.	unverified	0	�tats-unis	1	0.0

415	5 in 1 machine widely used agricultural machinery small rice farming equipment mini crawler tractor	1	1	250	1		0	5.0	9.0	5.0	5.0	1	1	1	1	899.0	3750.0	maxtrade inc	unverified	2	�tats-unis	1	0.0

416	35hp agricultural weeding latest agricultural machine in farm	1	1	251	1		0	4.6	189.0	4.6	4.5	1	1	1	1	1200.0	1300.0	weifang giant agricultural equipment co., ltd	unverified	0	chine	1	0.0

417	small farm agricultural garden tank sprayers 60l trolley type 1.1kw motor electric power pump sprayer machine	1	1	252	1		0	4.2	9.0	4.3	4.3	1	1	1	1	154.14	166.0	evangel industrial (shanghai) co., ltd.	unverified	0	chine	1	0.0

418	massey ferguson tractor agricultural machinery & equipment 120hp used farm tractor	1	3	223	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9999.0	12000.0	henan lvlong industrial co., ltd.	unverified	1	chine	1	5.0

419	dry land laser gps leveler agricultural leveling machine	1	1	253	1	CE	0	3.7	6.0	4.0	4.1	1	1	1	1	4400.0	5900.0	shenzhen aslin industry and trade co., ltd.	unverified	0	chine	1	0.0

420	agricultural machinery and equipment long using life farming machinery rotary tiller for sale	1	1	254	1		0	5.0	1.0	5.0	5.0	1	1	1	1	2000.0	2000.0	henan tangchao jinda trading company ltd.	unverified	1	chine	4	4.7

421	meiqi 186rt ditcher tillers farm machinery agriculture machinery used+cultivators	1	1	255	1		0	5.0	1.0	5.0	5.0	1	1	1	1	600.0	760.0	nanjing runshangwei technology co., ltd.	unverified	0	chine	2	3.2

422	agriculture machinery equipment peanut picker groundnut picking machine	1	1	256	1		0	3.8	16.0	4.0	3.9	1	1	1	1	850.0	2650.0	heze zhongming international trade co.,ltd	unverified	0	chine	1	0.0

423	new product factory poultry farming poultry equipment feed processing machines for agricultural machinery &equipment	1	1	257	1		10	5.0	9.0	5.0	5.0	1	1	1	1	629.0	659.0	henan baba trading co., ltd.	unverified	1	chine	2	4.9

424	poultry feeding agricultural machinery automatic self-priming corn mill machine garins maize flour grinder machine	1	1	258	1		0	0.0	0.0	0.0	0.0	1	1	1	1	145.0	185.0	yancheng luckystar import & export co., ltd.	unverified	0	chine	16	5.0

425	organic fertilizer ball granulation machine from agriculture machinery equipment	1	1	259	1		0	0.0	0.0	0.0	0.0	1	1	1	1	13000.0	13000.0	henan wonderful industrial co., ltd.	unverified	0	chine	11	0.0

426	high performance agricultural sprayer machine tractor 3 point boom sprayer machine	1	1	167	1		7	4.6	10.0	4.4	4.4	1	1	1	1	360.0	890.0	etablissements mano	unverified	2	france	2	0.0

427	second hand tractors kubota l425 50hp for sale cheap farm tractors agricultural machinery japan imported	1	1	120	1		1	4.8	36.0	4.8	4.7	1	1	1	1	2500.0	2500.0	shandong aolan drone science and technology co., ltd.	unverified	1	chine	3	5.0

428	used farm agriculture machinery & equipment massey ferguson yto lovol iseki df kubota 4x4 tractors 4wd for agriculture sale	1	1	260	1		0	5.0	3.0	5.0	5.0	1	1	1	1	7800.0	7800.0	syndmon international co., ltd.	unverified	0	chine	15	5.0

429	agriculture machinery ditcher	1	1	261	1		0	4.2	23.0	4.4	4.6	1	1	1	1	620.0	650.0	senoc point-of-sale marketing	unverified	2	philippines	4	0.0

430	massey ferguson tractor agricultural machinery / farm tractor available	1	1	262	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	5000.0	hunan jinsong machinery co., ltd.	unverified	0	chine	7	0.0

431	2in 1 sprayer pumps agricultural machinery 16l backpack farm lithium battery powered mist 20l electric knapsack sprayer	1	10	263	1		0	5.0	2.0	5.0	5.0	1	1	1	1	13.5	15.0	mafal (shanghai) machinery limited	unverified	1	chine	6	5.0

432	agricultural machinery/farm equipment/mini rotary tiller cultivator	1	1	115	1		0	5.0	2.0	5.0	5.0	1	1	1	1	455.0	520.0	rt g trading llc	unverified	1	�tats-unis	1	0.0

433	new self-propelled agricultural seedling transplanting machine greenhouse seedling planting machine	1	1	264	1		0	4.6	12.0	4.6	4.5	1	1	1	1	1089.55	1268.65	henan manxon machinery equipment co., ltd.	unverified	0	chine	8	5.0

434	hhd agriculture machinery equipment 8hp diesel farm walking tractors with rotary tillage machine	1	1	265	1		18	4.7	49.0	4.7	4.7	1	1	1	1	625.0	625.0	linyi wali machinery co., ltd.	unverified	0	chine	7	0.0

435	hand-push adjustable seeder agricultural machinery agricultural machinery agriculture equipment and tools	1	1	266	1		17	4.6	21.0	4.6	4.6	1	1	1	1	45.0	50.0	zhecheng hongxin machinery factory	unverified	0	chine	12	3.6

436	wholesale price seed planting and cultivating plastic mulching laying machine/plastic film land covering agricultural machinery	1	1	267	1		6	4.7	4.0	4.9	5.0	1	1	1	1	500.0	600.0	zhengzhou ohfu industry enterprise co., ltd.	unverified	1	chine	12	4.6

437	high durable agricultural sprayer pumps along with versatile agricultural sprayer machines for efficient agricultural operations	1	1	226	1		0	5.0	5.0	4.8	4.8	1	1	1	1	95.0	95.0	zhejiang gtm hi-tech intelligent equipment co., ltd.	unverified	0	chine	19	0.0

438	hand held motor back rotary power tiller for orchard arable land rotavator in agriculture manual weeder hoe ridging machine	1	1	268	1		0	0.0	0.0	0.0	0.0	1	1	1	1	179.0	539.0	yucheng hengshing machinery co., ltd.	unverified	0	chine	11	0.0

439	4x4 tractor with loader and backhoe agricultural machinery & equipment tractor 4wd farm tractor with epa engine and front loader	1	1	112	1		0	0.0	0.0	0.0	0.0	1	1	1	1	15000.0	15000.0	henan kellen machinery equipment co., ltd.	unverified	3	chine	8	4.7

440	self propelled mist air blow sprayer power agro agricultural sprayers machine	1	1	221	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1390.0	1520.0	taian hi-tech sunrise machinery co., ltd.	unverified	3	chine	9	5.0

441	cultivator agricultural machinery high quality and efficiency cultivator with roller made in turkey	1	1	269	1		0	0.0	0.0	0.0	0.0	1	1	1	1	600.0	2000.0	y j k trading plc	unverified	2	�thiopie	9	0.0

442	agriculture machine new hot sales tractor cultivator	1	1	220	1		1	5.0	1.0	5.0	5.0	1	1	1	1	438.0	438.0	laizhou yisu machinery co., ltd.	unverified	0	chine	2	0.0

443	spraying equipment boom sprayer farm sprayer boom agriculture sprayer spray boom tractor	1	1	127	1		0	1.8	3.0	2.1	2.3	1	1	1	1	5600.0	6000.0	yantai rima machinery co., ltd.	unverified	5	chine	7	4.7

444	used advance new holland 120hp snh1204 agricultural tractor / original quality new-holland agricultural farm tractor	1	1	15	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3900.0	3900.0	yongkang maxpower technology co., ltd.	pro	2	chine	2	4.9

445	chalion farm wheel tractor hole digger agriculture machine agriculture farm tractor mounted post hole digger earth auger price	1	10	13	1		1	5.0	8.0	5.0	5.0	1	1	1	1	700.0	800.0	qingzhou topone heavy industry co., ltd.	verified	3	chine	2	4.9

446	mini tractor 25 30 35 40 45 50 60 hp 4 wheel drive 4wd farming agriculture compact farm tractores agricolas tractor	1	1	218	1		0	5.0	4.0	5.0	5.0	1	1	1	1	2000.0	2100.0	shandong huayao construction machinery co., ltd.	unverified	2	chine	4	5.0

447	2024 trending product agricultural equipment cultivator rubber track multipurpose high power mini farm machine crawler tractor	1	1	225	1		0	4.7	28.0	4.6	4.4	1	1	1	1	4105.0	4105.0	ningbo wuheng electrical appliances co., ltd.	unverified	0	chine	2	5.0

448	buy original used second hand massey ferguson tractors fm390 agricultural machinery compact farm tractor for sale at low cost	1	1	216	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1800.0	2300.0	shandong guomaoguotai reducer co., ltd.	unverified	1	chine	17	5.0

449	japanese used tractors kubota 4x4 farming machine agricultural tractor agricola used kubota tractor	1	1	121	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	1500.0	zhejiang larissa mechanical electric technology co., ltd.	unverified	3	chine	7	4.2

450	factory direct supply mango grape sprayer agriculture machinery equipment sprayer	1	1	221	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1120.0	1190.0	north machinery (shandong) corporation	unverified	4	chine	3	4.4

451	mf 5480 tractor farm equipment 4wd used massey ferguson 5480/5480 tractor for agriculture	1	10	217	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	4500.0	celec enterprises	unverified	2	inde	16	0.0

452	agriculturalgasoline small rotary tiller tiller multifunctional weeder field agricultural garden tools garden tiller cultivators	1	1	102	1		12	4.9	38.0	4.9	4.9	1	1	1	1	99.0	99.0	hunan weiyan machinery technology co., ltd.	unverified	2	chine	4	4.4

453	5e-954 model 95 horse power john'dere' 4x4 farm tractors agriculture used tractors for sale with in good condition	1	1	219	1		0	4.6	14.0	4.5	4.7	1	1	1	1	16500.0	16700.0	zhumadian jiuyi industry and trade co., ltd.	unverified	2	chine	3	4.7

454	farm equipment tractor farm trailer tractor agricultural tractors for agriculture used farm cultivator	1	1	222	1		3	5.0	5.0	5.0	5.0	1	1	1	1	3000.0	5000.0	shiva enterprise	unverified	2	inde	9	0.0

455	agricultural machine garden cultivator hand-held gasoline power tiller for farm	1	1	182	1		0	4.2	5.0	4.3	4.6	1	1	1	1	235.0	250.0	nanjing metalwell machinery equipment co., ltd.	verified	5	chine	6	5.0

456	agricultural machinery agricultural cultivator mini tractor power cultivator micro power garden cultivator rotary	1	1	268	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1130.0	1130.0	kaxifa plant protection machinery (taizhou) co., ltd.	unverified	0	chine	10	5.0

457	used farm tractor holland 110-90 fiat 6 cylinder compact orchard farm tractor agricultural equipment four wheel tractor	1	1	270	1		0	5.0	4.0	5.0	5.0	1	1	1	1	3000.0	6000.0	leshan dongchuan machinery co., ltd.	unverified	1	chine	8	4.8

458	24 disc harrow for tractor agricultural machinery for farm heavy duty	1	1	223	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2350.0	2360.0	chiever gmbh	unverified	2	allemagne	1	0.0

459	agriculture machinery no-tillage precision fertilizing corn seeder for sale	1	1	29	1		0	4.9	10.0	4.9	4.9	1	1	1	1	1000.0	1200.0	dezhou ouchen poultry equipment co., ltd.	unverified	1	chine	9	5.0

460	quality agriculture machinery combine harvester for rice and wheat combine harvester	1	1	209	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	4000.0	lungshing international trade co., limited	unverified	1	hong-kong	1	0.0

461	hotoka 52cc gasoline tiller cultivators rotavator power glough agriculture machine farming mini rotary tiller	1	50	20	1	CE	4	4.8	40.0	4.9	4.9	1	1	1	1	59.0	70.0	shandong jiulin import & export co., ltd.	unverified	1	chine	8	5.0

462	massey ferguson 8s-245 tractor agricultural machinery & equipment for sale	1	1	26	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	abjs	unverified	2	france	1	0.0

463	reaper binder machine other agricultural machinery & equipment olive harvesting machine farm gasoline	1	2	98	1		0	5.0	3.0	5.0	5.0	1	1	1	1	850.0	850.0	shandong shuangli international trading co., ltd.	unverified	3	chine	5	5.0

464	agricultural machine tractor mounted mulch applicator machine	1	2	224	1		0	4.5	2.0	4.5	4.5	1	1	1	1	500.0	700.0	henan junzheng import and export co., ltd.	unverified	1	chine	3	5.0

465	zzgd best price whole feeding rice and wheat combine harvester agricultural machinery	1	1	149	1		0	3.8	58.0	3.7	3.6	1	1	1	1	4886.0	4886.0	shandong changsheng construction machinery co., ltd.	unverified	0	chine	12	0.0

466	top quality front end loader use farm tractor best agricultural machinery at latest discounted price	1	1	123	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2090.0	2682.0	guangzhou huitong machinery co., ltd.	unverified	3	chine	5	4.8

467	professional ditching agriculture machinery&equipment hand rotary power tiller cultivators	1	1	212	1		0	4.5	2.0	4.8	5.0	1	1	1	1	515.0	550.0	ever-power industry pte. ltd.	unverified	2	singapour	7	0.0

468	agricultural machinery silage/hay/straw tractor square balers machine silage packing machine	1	1	18	1		0	4.5	14.0	4.5	4.5	1	1	1	1	7400.0	7600.0	om power engineers	unverified	0	inde	9	0.0

469	used tractors cnh case farmall 125a 125hp 4x4wd agricultural machinery & equipment tracteur agricole massey ferguson tractors	1	1	120	1		0	4.8	36.0	4.8	4.7	1	1	1	1	4250.0	4250.0	qingdao evergrand international trade co., ltd.	unverified	1	chine	10	0.0

470	massey ferguson 390 agricultural machinery / new 85hp mf390 farm tractor	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0	laizhou kongze electronic equipment co.,ltd.	unverified	0	chine	1	0.0

471	used tractor kubota m954q m954 95hp cabin orchard compact japanese tractor agricola agricultural farm machinery	1	1	150	1		0	5.0	1.0	5.0	5.0	1	1	1	1	4400.0	6700.0	nanjing new donor machinery equipment co., ltd.	unverified	0	chine	4	5.0

472	agriculture machinery equipment professional technology electric wet peanut picker machine	1	1	211	1		0	0.0	0.0	0.0	0.0	1	1	1	1	735.0	785.0	jiaozuo newest machinery co., ltd.	unverified	1	chine	9	4.2

473	garden tools agriculture machinery deep tillage cultivator power tiller box engine packing	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	330.0	355.0	henan bedo machinery equipment co., ltd.	unverified	2	chine	12	5.0

474	top quality agricultural machinery 4wd tractors 80hp with ce certificate	1	1	152	1		3	4.5	12.0	4.4	4.5	1	1	1	1	7999.0	8999.0	chongqing motivity import and export co., ltd.	unverified	0	chine	2	0.0

475	high efficiency sugarcane agricultural machinery straw crusher machine tractor driven sugarcane straw crushing machine	1	1	153	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	2750.0	zhengzhou oski machinery co., ltd.	unverified	1	chine	3	5.0

476	new design machine sprayer knapsack sprayer agriculture machine insecticide spray machine	1	1	109	1		0	4.1	40.0	4.2	4.3	1	1	1	1	79.0	91.0	ssj group pte. ltd.	unverified	2	singapour	6	0.0

477	china top small chinese farm best tractor agriculture mini traktor cheap tractor 4x4 agriculture machine	1	1	119	1		0	4.8	12.0	4.8	4.8	1	1	1	1	1300.0	1600.0	hefei branagh photoelectric technology co., ltd.	unverified	0	chine	7	0.0

478	single track micro cultivators agricultural machinery farm equipment gasoline diesel cultivators	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	201.6	252.0	hebei julite sorting technology co., ltd.	unverified	0	chine	15	0.0

479	mini tractor agricultural machinery light rotary tiller rototiller chain drive for farm and home use	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	452.0	452.0	weifang luke machinery co., ltd.	unverified	0	chine	12	0.0

480	tramini tractor, agricultural machine,lk124/154/184/204 12hp 15hp 18hp 20hp	1	1	156	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1299.0	1299.0	hangzhou papaya trading co., ltd.	unverified	0	chine	11	0.0

481	best heavy rice planter agriculture machine used japan products	1	1	36	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	15000.0	aa auto truck otomotiv ihracat limited sirketi	unverified	2	turquie	2	0.0

482	tx best selling factory price sheller corn thresher machine maize sheller single row mini corn harvester with peelers china	1	5	33	1		4	5.0	7.0	5.0	5.0	1	1	1	1	45.0	50.0	yongkang xinghu power machinery co., ltd.	unverified	1	chine	15	5.0

483	second hand tractors 185hp 140hp 120hp 4wd tractor agricultural farm john deer tractor with rotary machine	1	1	48	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	3000.0	shijiazhuang daoliangmou trade co., ltd.	unverified	0	chine	7	5.0

484	hot sale home flour milling machine combine rice mill machine	1	1	157	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1050.0	1150.0	yucheng leyuan machinery co., ltd.	unverified	0	chine	12	0.0

485	chinese high quality tiller cultivator for small garden rotary crawler tractor machine for sale	1	1	158	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1690.0	1690.0	kaifeng hyde machinery co., ltd.	unverified	2	chine	9	3.0

486	electric small scale sorghum soybean paddy rice wheat peeler /corn sheller thresher machine	1	3	14	1		0	4.8	124.0	4.7	4.7	1	1	1	1	475.0	485.0	shandong horsen international industry co.,ltd	unverified	0	chine	4	0.0

487	agricultural machine parts compact tractor disc harrow heavy duty trailed disk plough machine	1	5	271	1		0	0.0	0.0	0.0	0.0	1	1	1	1	860.0	860.0	wenling whachinebrothers machinery co., ltd.	unverified	0	chine	3	0.0

488	strong used original kubota tractor for sale-agricultural machinery tractors	1	1	272	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1114.8	1672.2	weifang longtao machinery co., ltd.	unverified	0	chine	6	4.8

489	john deere- tractor premium quality original john deer agricultural machinery tractors available for sale	1	1	273	1		0	0.0	0.0	0.0	0.0	1	1	1	1	12000.0	15000.0	xingtai xiangwei commercial co., ltd.	unverified	3	chine	2	4.9

490	30-180hp 4wd best agriculture fendt tractor	1	1	274	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4500.0	4500.0	tradella international	unverified	2	inde	4	0.0

491	mini tractor sold lawn mover tractor farm tractor 4x4 agricultural	1	1	275	1		0	5.0	10.0	5.0	5.0	1	1	1	1	1500.0	1500.0	changzhou fengqing mechanical and electrical equipment co., ltd.	unverified	0	chine	11	0.0

492	all kinds of disc harrow blades agriculture farming machinery equipment spare parts plow blades	1	1	276	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9.9	9.9	nanjing bang win imp & exp co., ltd.	unverified	1	chine	6	1.0

493	25hp 30hp 35hp 40hp 45hp 50hp 60hp 70hp 80hp tractor agricultural mini tractor with cabin	1	1	277	1		0	3.4	9.0	3.5	3.6	1	1	1	1	2000.0	2000.0	weifang pengzhan agricultural science and technology co., ltd.	unverified	0	chine	1	0.0

494	new round mini agricultural machinery equipment hay straw baler for tractor	1	1	278	1		0	5.0	4.0	5.0	5.0	1	1	1	1	4000.0	4000.0	wl immo invest	unverified	2	france	1	0.0

495	professional self-propelled high clearance boom agricultural sprayer	1	1	279	1		0	0.0	0.0	0.0	0.0	1	1	1	1	13800.0	13800.0	jiangsu jiuheng agricultural machinery development co., ltd.	unverified	0	chine	1	0.0

496	agricultural machine spare parts agricultural bean harvesting alfalfa reaper mini corn silage harvester machine	1	2	280	1		0	0.0	0.0	0.0	0.0	1	1	1	1	280.0	323.0	sarl bado 2	unverified	2	france	2	0.0

497	intelligent remote control agricultural machinery used home and farm use robot lawn mower with automatic engine and pump	1	1	281	1		0	4.8	28.0	4.8	4.8	1	1	1	1	1150.0	1150.0	zhengzhou fusion machinery co., ltd.	unverified	3	chine	11	5.0

498	agricultural high flow rate high pressure gasoline sprayer pump	1	1	282	1		0	5.0	2.0	4.8	4.5	1	1	1	1	26.8	26.8	erreppi srl	unverified	1	italie	3	0.0

499	farmland machinery equipment center pivot irrigation system agriculture lateral linear move side roll irrigation system	1	1	283	1		0	5.0	3.0	5.0	5.0	1	1	1	1	8000.0	8000.0	linyi fengrui plant protection electronic equipment co., ltd.	unverified	1	chine	9	4.6

500	4wd 4x4 30hp 50hp 80hp 120hp mini farm tractors used kubota agriculture farm machinery cheap farm tractor for sale	1	1	284	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	2200.0	quzhou surri import and export trading co., ltd.	unverified	1	chine	11	5.0

501	feed pellet mill dies for the sale of pellet mill spare parts for agricultural companies	1	1	285	1		0	4.6	34.0	4.6	4.6	1	1	1	1	46.0	46.0	zhengzhou runxiang machinery equipment co., ltd.	unverified	2	chine	8	5.0

502	agricultural machine parts walking tractor tiller machine weeding wheel	1	10	286	1		1	4.8	5.0	4.4	4.2	1	1	1	1	35.0	40.0	huai'an runchi machinery co., ltd.	unverified	1	chine	2	4.8

503	xifa high quality wheat combine harvester wheat harvesting machine in pakistan wheat mini harvest machine	1	1	237	1		0	4.4	15.0	4.4	4.4	1	1	1	1	586.0	658.0	henan tianzhong machinery co., ltd.	unverified	1	chine	5	5.0

504	cassava root harvester herb harvester machine onion garlic harvest machine	1	1	166	1		0	4.2	16.0	4.2	4.1	1	1	1	1	280.0	280.0	shandong guansen agricultural technology co., ltd.	unverified	0	chine	1	0.0

505	poultry/livestock farm chicken duck and goose feed pellet production line 3-4ton animal feed pellet machine	1	1	287	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2601.0	3860.0	henan banglan machinery co., ltd.	unverified	1	chine	2	4.7

506	machine,cultivators agricultural farming,tiller cultivator mini rotary power farming equipment agricultural cultivator	1	1	288	1		0	0.0	0.0	0.0	0.0	1	1	1	1	339.0	510.0	nanchang ychipre machinery co., ltd.	unverified	1	chine	4	4.8

507	agricultural small multifunctional rotary tiller gasoline orchard weeding and turning machine ditching and loosening machine	1	1	289	1		0	0.0	0.0	0.0	0.0	1	1	1	1	106.0	106.0	shandong blackwolf machinery co., ltd.	unverified	2	chine	3	5.0

508	agricultural machinery big horsepower kat2004 tractor with high quality	1	1	290	1		0	5.0	13.0	5.0	5.0	1	1	1	1	3000.0	6500.0	xinxiang chenwei machinery co., ltd.	unverified	2	chine	12	5.0

509	agriculture machinery customized mini round baler hay straw round net baler mrb0850 round baler for sale	1	1	291	1		70	4.8	93.0	4.6	4.5	1	1	1	1	2000.0	2250.0	bigbund (shanghai) construction machinery co., ltd.	unverified	5	chine	7	4.6

510	agricultural small multi-functional gasoline hand-held cultivated land loosening machine rotary tiller micro-tiller	1	1	16	1		18	4.5	30.0	4.5	4.5	1	1	1	1	99.0	99.0	shijiazhuang xianghang agricultural machinery co., ltd.	unverified	0	chine	2	5.0

511	2020 tractor john dee 95hp 100hp 120hp 140hp tractor jon deer jd1204 farm machinery farm tractor	1	1	163	1		0	0.0	0.0	0.0	0.0	1	1	1	1	17300.0	17300.0	ningbo liangye electric appliances co., ltd.	unverified	5	chine	4	5.0

512	agricultural implement light and middle duty tractor mounted 16 blade disc harrow for sale	1	1	292	1		0	4.8	14.0	4.7	4.6	1	1	1	1	359.0	359.0	lsw  immobilien gmbh	unverified	2	allemagne	2	0.0

513	mgcz60*20 rice mill agriculture machine paddy separator separador de arroz	1	1	74	1		0	3.8	6.0	4.0	4.0	1	1	1	1	2880.0	2880.0	weifang taishan tractor co., ltd.	unverified	0	chine	4	0.0

514	agricultural mini diesel motorcycle power cultivator two-wheel walking tractor multifunctional tractor price farm land	1	1	232	1		3	3.1	8.0	3.2	3.3	1	1	1	1	684.0	684.0	beijing taishan guotai import export co., ltd.	unverified	0	chine	9	5.0

515	agriculture equipment farming machinery agricultural cultivators	1	1	293	1		0	4.8	11.0	4.6	4.6	1	1	1	1	260.0	530.0	hangzhou ever-power transmission co., ltd.	unverified	1	chine	17	5.0

516	high quality boom tractor diaphragm pump intelligent agricultural sprayer	1	1	253	1	CCC,CE	0	3.7	6.0	4.0	4.1	1	1	1	1	280.0	320.0	abc global corporation	unverified	2	�tats-unis	1	0.0

517	made in china factory price agricultural equipment farm machinery traktor 4x4 mini farm 4wd 25hp compact tractor	1	1	294	1	CE	6	5.0	30.0	5.0	5.0	1	1	1	1	5500.0	5710.0	cixi nofia machinery factory	unverified	0	chine	11	0.0

518	yto tractor lx804 small farmer walking tractor for agriculture mini tractor	1	1	295	1		0	4.0	1.0	4.3	4.0	1	1	1	1	7500.0	8000.0	wuhan macton machine co., ltd.	unverified	1	chine	6	5.0

519	cheap kubota tractor tractor 290 mf 385 and mf 390 agriculture machine farm tractor kubota for sale at affordable prices	1	1	296	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2500.0	yangzhou goose agricultural machinery co., ltd.	unverified	0	chine	4	0.0

520	buy new wheel kubota m7060 4wd wheel agricultural equipment tractor for cheap sales	1	1	40	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2200.0	2200.0	weifang yishan heavy machinery co., ltd.	unverified	1	chine	8	5.0

521	wholesale used agricultural tractors four-wheel plows and motorcycle cultivator fruit trees producing hp tractor	1	1	196	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3580.0	4500.0	global trade de gmbh	unverified	2	allemagne	3	0.0

522	china agriculture machinery hydraulic heavy duty disc harrow	1	3	91	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1100.0	2000.0	huzhou liangyi construction co.,ltd	unverified	1	chine	6	5.0

523	tractor 3 point landscape rake for sale. agricultural machinery equipments, spike rake pine straw	1	1	297	1		1	4.6	13.0	4.6	4.5	1	1	1	1	260.0	360.0	zhengzhou pasen machinery co., ltd.	unverified	1	chine	5	5.0

524	high pressure sector nozzle fan-shaped spray gun garden irrigation fog sprinkler head agricultural sprayer	1	1	298	1		1	0.0	0.0	0.0	0.0	1	1	1	1	7.0	7.0	weifang austter industry and trade co., ltd.	unverified	0	chine	4	0.0

525	lutian china cheap 50hp 60hp 70hp 4wd mini small wheeled tractors mini tractor for agriculture	1	1	299	1		2	0.0	0.0	0.0	0.0	1	1	1	1	800.0	800.0	liyang jize machinery co., ltd.	unverified	0	chine	3	0.0

526	seed planting fertilizing machine hand push seeder agriculture fertilizer and seeder manufacturers	1	10	300	1		10	4.2	30.0	4.4	4.6	1	1	1	1	56.0	110.0	eurl verne	unverified	2	france	1	0.0

527	high quality rice mill machine price philippines rice mill for sale rice grinder machine molino de arroz	1	1	85	1		0	4.0	5.0	4.0	4.0	1	1	1	1	169.0	249.0	jining jinmei machinery co., ltd.	unverified	0	chine	1	0.0

528	agricultural machinery tractor rear blade land leveling hydraulic scraper grader	1	1	301	1		26	0.0	0.0	0.0	0.0	1	1	1	1	1028.0	1083.0	seven11 llc	unverified	2	�tats-unis	1	0.0

529	244 model 24hp 4wd tractor agriculture machinery small farm tractor with cultivator	1	1	302	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1200.0	3200.0	baoding montage trading co., ltd.	unverified	0	chine	1	0.0

530	rotary cultivator diesel engine petrol mini rototiller farm machinery tractor rear tine power tiller for agriculture in kenya	1	1	303	1		1	4.3	50.0	4.4	4.4	1	1	1	1	369.0	553.0	shandong mingda machinery co., ltd.	unverified	1	chine	2	5.0

531	agricultural corn thresher and skin removing /wheat thresher rice and maize threshing/corn sheller	1	1	304	1		0	0.0	0.0	0.0	0.0	1	1	1	1	336.0	336.0	laizhou xixin machinery co., ltd.	unverified	1	chine	4	5.0

532	7.5hp 25hp tractor power tiller walking tractor agricultural machine walking tractor harvester	1	1	305	1		0	4.9	23.0	4.8	4.7	1	1	1	1	469.0	723.8	shanghai henotec industrial co.,ltd	unverified	3	chine	4	4.6

533	agricultural machinery tractor	1	1	306	1		1	4.8	90.0	4.7	4.7	1	1	1	1	8000.0	8000.0	zhengzhou mingding mechanical equipment co., ltd.	unverified	0	chine	3	0.0

534	agricultural machinery single furrow mouldboard plough furrow plough	1	1	170	1		0	4.8	6.0	4.6	4.6	1	1	1	1	522.11	654.76	sprl paan trade	unverified	2	belgique	1	0.0

535	hhd new wsft151-20 mini and other agricultural machinery planter for walking tractor	1	1	265	1		18	4.7	49.0	4.7	4.7	1	1	1	1	860.0	860.0	qingdao lezi industry and trade co., ltd.	unverified	0	chine	2	0.0

536	agricultural powered diesel generator two wheel farm tractor 22hp 25hp tractor power tiller walking tractor powertiller	1	1	307	1		0	5.0	1.0	5.0	5.0	1	1	1	1	780.0	780.0	shandong yilu machinery co., ltd	unverified	0	chine	2	0.0

537	brand agriculture 80hp tractor with front end loader 4 in 1 bucket lt804b	1	1	308	1		0	5.0	10.0	5.0	5.0	1	1	1	1	12850.0	13250.0						

538	joyance chinese manufacturer hot sale wireless zero turn grass cutter remote control gasoline lawn mower agriculture sprayer	1	1	76	1	CE	0	5.0	20.0	5.0	5.0	1	1	1	1	999.0	1600.0						

539	tractor agricultural machinery tractor 4wd 50hp 60hp 70hp 80hp 90hp 100hp agricultural with front end bucket	1	1	234	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1299.0	7999.0						

540	epa engine agricultural machine tractor 4wd 25hp power on top selling	1	1	309	1		0	4.5	30.0	4.5	4.5	1	1	1	1	4500.0	8800.0						

541	latest agriculture machine hand held weeder 30cm width	1	50	310	1		6	4.4	21.0	4.2	4.1	1	1	1	1	155.0	170.0						

542	very cheap products cost effective agricultural machinery equipment 50hp farm crawler tractor	1	1	311	1		2	4.2	50.0	4.3	4.4	1	1	1	1	4890.0	4890.0						

543	better two wheel mini farm tractor for agriculture machinery equipment with tiller cultivator	1	1	312	1		0	4.3	118.0	4.4	4.4	1	1	1	1	620.0	660.0						

544	agricultural maize seeder drill 4 rows maize planter with fertilizer corn recise seeder	1	1	313	1		0	0.0	0.0	0.0	0.0	1	1	1	1	75.0	100.0						

545	small hand held cultivators agricultural rotary tiller weeder cultivator equipment	1	1	314	1		0	4.9	15.0	4.7	4.6	1	1	1	1	400.0	556.0						

546	mini farm agriculture tractors 4wd 140hp 4x4 drive mini wheel tractor	1	1	4	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3630.0	8509.0						

547	kubota m854kq agricultural cultivator tractor kubota tractors price list for sale farm japan tractor	1	2	315	1		0	0.0	0.0	0.0	0.0	1	1	1	1	200.0	500.0						

548	promotional high quality farm machine heavy duty rotary cultivator rotary tiller	1	2	148	1		0	5.0	12.0	5.0	5.0	1	1	1	1	1400.0	1400.0						

549	18hp two wheel farm walking tractor 22hp mini hand tractors for agriculture	1	10	316	1		0	0.0	0.0	0.0	0.0	1	1	1	1	400.0	1000.0						

550	hot sale farm machinery equipment multifunctional tractors prices 4wd 130hp 140hp 150hp 4x4 yto 50 hp engine tractors	1	1	317	1		0	5.0	13.0	5.0	5.0	1	1	1	1	5500.0	6990.0						

551	new agricultural machinery chaff cutter grass feed chopper machine for farms manufacturing plants engine motor core components	1	50	68	1		0	0.0	0.0	0.0	0.0	1	1	1	1	180.0	180.0						

552	china mini tractores agricolas farm garden tractors 4x4 attachments loader machine agricultural machinery for sale	1	1	236	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3999.0	9999.0						

553	agricultural machinery tractor agricultural boom spray machine ce certification	1	1	318	1		0	4.5	2.0	4.3	4.0	1	1	1	1	5000.0	5000.0						

554	85 hp farm tractor hwb 854 agricultural machinery hot sale	1	1	319	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8500.0	12500.0						

555	lg2023- agricultural machinery, fully automatic lawn mower, agricultural machinery products	1	1	320	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	3500.0						

556	direct supplier hay cutting 3 point topper mower tractor farm tractor agricultural machinery walking tractor machinery	1	5	71	1		0	0.0	0.0	0.0	0.0	1	1	1	1	400.0	450.0						

557	agricultural machinery and equipment4-cylinder engine 70hp tractor	1	1	72	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8000.0	8000.0						

558	25hp mini wheel tractor 25 hp mini tractor agricultural machinery 25hp mini tractors	1	1	222	1		0	5.0	5.0	5.0	5.0	1	1	1	1	1100.0	2000.0						

559	best selling agricultural machinery peanut picker peanut harvester machine for sale	1	1	321	1		0	4.5	11.0	4.4	4.3	1	1	1	1	850.0	965.0						

560	poultry cow dung dewatering machine solid cow manure dehydrator machine	1	1	322	1		5	4.0	17.0	4.1	4.1	1	1	1	1	1200.0	1200.0						

561	remote control diesel mini tiller cultivator farm equipment management agricultural machinery	1	1	241	1		0	4.6	10.0	4.2	3.7	1	1	1	1	900.0	1000.0						

562	massey ferguson mf290 4x4 wheel drive agricultural farm tractors	1	1	323	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1200.0	1200.0						

563	auto mini rice mill business rice flour grinding machine rice milling machine	1	1	324	1		5	3.0	2.0	3.0	3.0	1	1	1	1	260.0	350.0						

564	high efficiency hemp sisal fiber extraction kenaf abaca fiber extractor decorticator machine hemp peeling machine	1	1	75	1		1	5.0	17.0	5.0	5.0	1	1	1	1	1200.0	1300.0						

565	farm tractor 3-point mounted 3 rows corn seeder corn planter machine	1	1	325	1		0	5.0	3.0	5.0	5.0	1	1	1	1	768.0	857.0						

566	china agricultural machinery manufacturer 4wd 80hp 90hp 100hp cheap wheel mini farm tractor with front end loader and backhoe	1	1	19	1		0	4.8	9.0	4.7	4.6	1	1	1	1	9900.0	10000.0						

567	good quality agricultural machinery & equipment light rotary tiller suitable for both wet and dry fields	1	10	107	1		292	4.8	8.0	4.7	4.5	1	1	1	1	1043.0	1064.0						

568	2023 newly arrival construction equipment front end loader use agricultural machinery at best price	1	1	123	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2090.0	2682.0						

569	manufacturer to offer good agriculture machinery combine harvester for corn in china	1	1	130	1		0	5.0	1.0	5.0	5.0	1	1	1	1	32500.0	33000.0						

570	used/second hand/new wheel tractors 4x4wd td5110 110hp with small mini compact farm equipment agricultural machinery	1	1	127	1		0	1.8	3.0	2.1	2.3	1	1	1	1	6400.0	6500.0						

571	agriculture machinery and equipment grain processing sesame seed cleaning machine	1	1	101	1		0	5.0	3.0	5.0	5.0	1	1	1	1	9000.0	9500.0						

572	agriculture machinery maize clover willow corn silage reaper machine	1	1	103	1		0	4.7	3.0	4.8	4.6	1	1	1	1	880.0	1250.0						

573	anon 2024 new 70-260hp wheel tractors 4x4 4wd agricultural front loader tractor agricultural machinery	1	1	114	1		0	5.0	5.0	4.7	4.2	1	1	1	1	1200.0	1599.0						

574	used/second hand/new wheel tractors 4x4wd johnn deer 5e 1004 100hp with small mini compact farm equipment agricultural machinery	1	1	120	1		0	4.8	36.0	4.8	4.7	1	1	1	1	8965.0	8965.0						

575	new design best wholesale farm boom sprayer 500l 1000l pump marketing equipment agricultural machinery now available for sale	1	1	167	1		0	4.6	10.0	4.4	4.4	1	1	1	1	140.0	878.0						

576	crawler tractor farm orchard paddy field/mini tractor with rotary tiller plow various agricultural machinery	1	1	132	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	1190.0						

577	small agriculture machinery qln-354 small tractor mini tractor 4x4 35hp mini garden farm tractor cultivator machine in malaysia	1	1	13	1	CE	0	5.0	8.0	5.0	5.0	1	1	1	1	4500.0	4500.0						

578	factory price new micro supply crawler traktor mini tractors 4x4 agricultural tractor agriculture machine	1	1	119	1		0	4.8	12.0	4.8	4.8	1	1	1	1	2120.0	2230.0						

579	best price agricultural machinery/walking tractor with various of complement/agricultural equipment	1	1	109	1		0	4.1	40.0	4.2	4.3	1	1	1	1	599.0	659.0						

580	buy cheap clean new 120hp case ih tractor agricultural machinery 125a farm tractor agricultural tractor available now online	1	1	164	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	3500.0						

581	rc and hand push mower lawn mower mini agriculture machinery for agriculture	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	835.0	895.0						

582	diesel rotary tiller for orchard weeding and garden soil loosening farm equipment agricultural machinery weeder for gardens	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	317.49	354.84						

583	brush cutter price new agricultural machines with names and uses rotary tool kit cordless agri machine weeders	1	1	118	1		0	5.0	11.0	5.0	5.0	1	1	1	1	149.0	459.0						

584	good high quality best farm small tractor agricultural machinery	1	1	36	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7000.0	20000.0						

585	multifunctional agricultural tractor four wheel agricultural high quality tractor trailer agricultural machinery for sale	1	1	152	1		2	4.5	12.0	4.4	4.5	1	1	1	1	3500.0	4500.0						

586	best offer original massey ferquson tractor /used agricultural machinery tractor with original perkins engine available	1	1	216	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	4100.0						

587	new design mini farm tractor free shipping tractors mini 4x4 agriculture machine for sale chinese tractors prices	1	1	169	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1900.0	2800.0						

588	high efficiency strong practicality root/ginseng/ garlic harvesting low power cassava grain harvester agricultural machinery	1	1	153	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	1200.0						

589	200 liter sprayer agricultural machinery and equipment high pressure air sprayer	1	1	182	1		0	4.2	5.0	4.3	4.6	1	1	1	1	1725.0	1725.0						

590	used mini high quality agricultural machinery & equipment tractors lovol m804-b 80hp 4x4 tractor	1	1	162	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6200.0	6200.0						

591	tx mini power tiller 7hp cultivator subsoiler loose soil furrow ridge agricultural gasoline diesel tiller cultivators machine	1	1	33	1		0	5.0	7.0	5.0	5.0	1	1	1	1	115.0	125.0						

592	the latest agricultural machinery handheld weeding machines packaging machines for sale	1	1	154	1		0	0.0	0.0	0.0	0.0	1	1	1	1	20000.0	20000.0						

593	potato seeder for walking tractor planter agricultural machinery	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	202.0	202.0						

594	quality strong running 4wd farm tractor 90hp to 260hp agricultural machinery with water pump	1	1	327	1	CE	0	0.0	0.0	0.0	0.0	1	1	1	1	34180.0	34700.0						

595	agricultural machinery tractor tiller cultivator pto mini rotary power tiller	1	1	156	1		0	5.0	2.0	5.0	5.0	1	1	1	1	358.0	358.0						

596	agriculture machinery hand tractor hitch rotary 2 disc plough farm cultivator plow machine	1	1	157	1		1	5.0	2.0	5.0	5.0	1	1	1	1	260.0	330.0						

597	agriculture machinery farm ridging machine farm laminating machine	1	1	328	1		0	0.0	0.0	0.0	0.0	1	1	1	1	500.0	500.0						

598	hot sale farm equipment mini plow 2 wheel walking tractor with disc plough machine	1	1	14	1		23	4.8	124.0	4.7	4.7	1	1	1	1	290.0	290.0						

599	electric manual air selector electric agricultural grain rice tea rapeseed corn wheat cocoa bean winnowing machines	1	1	171	1		1	4.1	65.0	4.4	4.4	1	1	1	1	50.0	60.0						

600	manual hand corn thresher small household corn baler home use corn maize sheller husker machine husk peeling machine	1	1	158	1		12	5.0	2.0	5.0	5.0	1	1	1	1	2.0	2.0						

601	gasoline knapsack agricultural mist duster sprayer backpack powered garden blower machine with 20l/26l tank mist blower	1	1	128	1		1	4.7	37.0	4.7	4.7	1	1	1	1	49.9	57.0						

602	factory supply weeding machine maize weeding machine power weeder hot selling to africa	1	10	243	1		0	4.6	12.0	4.8	4.9	1	1	1	1	68.0	120.0						

603	rotary tiller micro-tiller agricultural small multi-functional gasoline hand-held cultivated land loosening machine	1	1	102	1		4	4.9	38.0	4.9	4.9	1	1	1	1	99.0	99.0						

604	backbone machinery high capacity corn thresher maize thresher with 7.5 hp gasoline engine	1	1	159	1		26	4.8	19.0	4.7	4.7	1	1	1	1	142.0	165.0						

605	china eurotrac farm tractor ph farm tractor iseki used farm equipment tractor machinery	1	1	160	1		0	4.8	3.0	4.7	4.6	1	1	1	1	20625.0	20625.0						

606	15hp four stroke cultivators agricultural farming garden cultivator mini tractor tiller rotary cultivation machine	1	1	252	1		0	4.2	9.0	4.3	4.3	1	1	1	1	148.57	167.14						

607	tractors farm mini track tractor 4x4 agricultural tractors	1	1	275	1		0	5.0	10.0	5.0	5.0	1	1	1	1	1500.0	1500.0						

608	used tractors ford 4x4 farming machine agricultural tractor	1	1	296	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3500.0						

609	52cc 6blade small agriculture rotary cultivator machine garden tools walk behind tiller garden cultivator	1	100	329	1	CE	10	4.8	12.0	4.8	4.9	1	1	1	1	91.0	95.0						

610	competitive price agricultural machine farm tractor garden rotary mini tiller cultivator power tillers	1	1	330	1		6	4.9	18.0	4.6	4.5	1	1	1	1	459.0	739.0						

611	used cheap massey ferguson tractor 290 , mf 385 and mf 390 agriculture machine farm tractor rated power (hp) 100hp	1	1	315	1		0	0.0	0.0	0.0	0.0	1	1	1	1	650.0	1000.0						

612	farm drone sprayer agriculture agricultural sprayer fumigation pumps provided farm equipment 5 hp irrigation pump htp spray pump	1	1	306	1		0	4.8	90.0	4.7	4.7	1	1	1	1	2600.0	2600.0						

613	large stock agricultural machinery harvester	1	1	331	1		0	3.0	3.0	3.5	4.0	1	1	1	1	500.0	500.0						

614	agriculture pressure sprayer	1	1	332	1		0	3.6	5.0	3.8	3.8	1	1	1	1	100.0	300.0						

615	new agriculture machine cultivator tractor cheap chinese tractor	1	1	333	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	15000.0						

616	5l 8l 10l 12l 16l china pandora make battery sprayer knapsack sprayer for garden sprayer agricultural pesticide spraying	1	600	334	1	CE	0	5.0	1.0	5.0	5.0	1	1	1	1	15.5	18.0						

617	4wd 4x4 30hp 50hp mini farm tractors agriculture farm machinery cheap farm tractor for sale	1	1	335	1		0	3.4	4.0	3.1	3.0	1	1	1	1	1000.0	1000.0						

618	25 directly connect high pressure gasoline pesticide sprayer pump petrol engine for agriculture equipment and tools	1	50	336	1		0	0.0	0.0	0.0	0.0	1	1	1	1	91.0	95.0						

619	yto elx804 farm walking tractor agricultural equipment prices tractors with rops multifunctional tractor engines 430 mm	1	1	337	1		2	4.3	21.0	4.3	4.3	1	1	1	1	4000.0	5000.0						

620	export thermal fogging sprayer mist fogger pesticide spray fogging machine agriculture portable thermal fumigation sprayers	1	10	338	1		4	4.6	8.0	4.5	4.5	1	1	1	1	80.0	95.0						

621	landtop easy to use field diesel tools farming equipment agricultural power tiller weeder cultivation for farmer	1	1	339	1		0	5.0	18.0	4.9	4.9	1	1	1	1	375.0	405.0						

622	agriculture machine grass cutter lawn mower	1	1	340	1		29	0.0	0.0	0.0	0.0	1	1	1	1	1449.0	1999.0						

623	agriculture 3 point hitch tractor backhoe	1	2	341	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1675.0	1750.0						

624	25 hp tractor agricultural machinery farm use	1	1	342	1	CE	0	4.8	12.0	4.8	4.6	1	1	1	1	3000.0	3900.0						

625	china agricultural machinery jinma 254 454 4x4 mini front end loader farm tractors with eec for sale in europe	1	1	343	1		0	4.0	1.0	4.6	5.0	1	1	1	1	6000.0	7000.0						

626	adjustable hand-push seeder/ agricultural machinery manual garden seeder/ agriculture equipment tools	1	1	344	1		0	4.6	68.0	4.7	4.8	1	1	1	1	40.0	50.0						

627	yto 220hp lx2204 tractor agricultural machine farm tractor 220hp tractor	1	1	345	1		0	4.5	6.0	4.6	4.6	1	1	1	1	64500.0	65500.0						

628	fendt agricultural tractor available at wholesale best price fendt 724	1	1	346	1		0	0.0	0.0	0.0	0.0	1	1	1	1	15000.0	17000.0						

629	agriculture machinery walking tractor 2 point disc plow 2 wheel plough machine cultivator 2 3 4 5 6 blades disc thailand	1	1	286	1		7	4.8	5.0	4.4	4.2	1	1	1	1	50.0	200.0						

630	1000l big agricultural self propelled boom sprayer	1	1	347	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	1000.0						

631	disinfection agriculture pest knapsack power sprayer 20l mist duster	1	100	348	1		0	0.0	0.0	0.0	0.0	1	1	1	1	50.0	53.0						

632	small agriculture machinery mini tiller wholesale high quality tillers cultivators	1	2	349	1		0	4.7	47.0	4.6	4.5	1	1	1	1	82.0	91.0						

633	original kubota tractor available for sale agricultural machinery tractors used and new	1	1	350	1		0	0.0	0.0	0.0	0.0	1	1	1	1	900.0	900.0						

634	disc harrow agricultural machinery farm tractor disc blade 2023	1	1	351	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3800.0	3850.0						

635	ce certification 70hp 4wd 4x4 farming agricultural top quality 3-point linkage tractor with swing draw bar free shipping	1	1	54	1		0	5.0	1.0	5.0	5.0	1	1	1	1	3800.0	3900.0						

636	2023 new type china agricultural machinery tractor	1	1	352	1		0	4.8	24.0	4.9	5.0	1	1	1	1	3699.0	3699.0						

637	4wd front wheel loader tractor 35hp agricultural mini tractor with excavator backhoe for sale	1	1	353	1		0	4.8	53.0	4.7	4.5	1	1	1	1	3899.0	4500.0						

638	hot selling mini tractor 4x4 for farming agriculture hydraulic tractor 80hp wheel tractor for sale	1	1	354	1		0	4.7	47.0	4.7	4.6	1	1	1	1	4300.0	4800.0						

639	fairly quality tractor farm tractor 80hp 4wd agriculture machinery equipment supplier ready for immediate shipment	1	1	355	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	3500.0						

640	agricultural maize seeder drill 4 rows corn planter with fertiliser corn precise seeder	1	1	356	1		0	0.0	0.0	0.0	0.0	1	1	1	1	300.0	500.0						

641	hot sale 2wd mini agricultural equipment featuring core engine and gearbox components walking tractor new plow for sale	1	1	357	1		0	0.0	0.0	0.0	0.0	1	1	1	1	200.0	400.0						

642	zoomlion mini farming 70hp 80hp 90hp 100hp 120hp 130hp 140hp 150hp tractor price agricultural tractor for front loader	1	1	358	1		0	5.0	7.0	5.0	5.0	1	1	1	1	14500.0	17500.0						

643	chinese famous brand yto agricultural tractor lg1504 150hp farm tractor for sale	1	1	359	1		0	5.0	3.0	5.0	5.0	1	1	1	1	20000.0	25000.0						

644	agricultural machine disc plow for tractor disc plough	1	5	273	1		0	0.0	0.0	0.0	0.0	1	1	1	1	320.0	430.0						

645	dongfeng iseki 95 hp en954c-pvcy agriculture tractor farming machine agriculture mini tractor	1	1	360	1		0	4.5	2.0	4.8	5.0	1	1	1	1	5000.0	10000.0						

646	agricultural sprayer spare parts manual knapsack sprayer accessores grip solo 425 handle sprayer trigger switch shut-off valve	1	100	361	1		0	0.0	0.0	0.0	0.0	1	1	1	1	0.5	3.0						

647	knapsack 2 stroke gasoline engine agriculture spray machine motor agricultural machinery equipment	1	20	362	1		0	4.9	76.0	4.8	4.8	1	1	1	1	52.95	62.85						

648	collapsible agriculture irrigation tank custom water storage tank for agricultural greenhouses	1	1	363	1		0	5.0	16.0	5.0	5.0	1	1	1	1	168.0	198.0						

649	2022 china huaxing yulin agricultural four wheel linear pivot irrigation/lateral move irrigation with fertilization system	1	1	364	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	10000.0						

650	factory direct sales hand-pushed corn peanut soybean planter multi-function agricultural seeder	1	1	365	1		0	5.0	2.0	5.0	5.0	1	1	1	1	41.0	41.0						

651	agriculture machine eft e410p 4 axis 10l brushless spraying gimbal system folding quadcopter	1	1	366	1		0	5.0	6.0	5.0	5.0	1	1	1	1	430.0	480.0						

652	agriculture machinery equipment small mini wheel tractor price tractor de agricultura	1	1	367	1		3	4.9	14.0	4.7	4.6	1	1	1	1	4700.0	9500.0						

653	multifunction crawler tractor quality assured mini crawler tractors agricultural tractor	1	1	281	1		0	4.8	28.0	4.8	4.8	1	1	1	1	1764.0	2158.0						

654	150 hp a/c cabin 4w farm tractor garden tractor, agricultural machinery factory direct sales, good price high quality	1	1	195	1		0	0.0	0.0	0.0	0.0	1	1	1	1	27500.0	28888.0						

655	fineyou ml8322 round bale machine hay baler professional agricultural machinery factory	1	1	142	1		0	0.0	0.0	0.0	0.0	1	1	1	1	22000.0	35000.0						

656	5xfz-25g grains multifunctional cleaner mobile seed sorting agricultural machinery farm equipment	1	1	368	1		0	5.0	9.0	5.0	5.0	1	1	1	1	8985.0	8985.0						

657	new running 4wd kubota tractor m9540 60hp 75hp 80hp 120hp farm tractor agricultural machinery available for sale..	1	2	31	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2798.0	3144.0						

658	industrial farm using grass cutter machine with multiple blade agriculture machine grass cutter electric petrol	1	1	369	1		2	4.9	16.0	4.8	4.7	1	1	1	1	230.0	250.0						

659	25hp 30hp 35hp 40hp tractors small cheap loader mini tractor agricultural machinery	1	1	25	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8700.0	8900.0						

660	modern agricultural machinery animal dung solid liquid separator dewatering machine	1	1	370	1		0	0.0	0.0	0.0	0.0	1	1	1	1	11700.0	12500.0						

661	tractor mounted agricultural equipment 1lyq disc plough/disc plow agricultural machine for sale	1	3	133	1		0	5.0	4.0	5.0	5.0	1	1	1	1	250.0	350.0						

662	chinese brand tractor best price 4x4 big tractor qln130hp farm tractor 130hp 4*4 modern agricultural machinery with low price	1	1	13	1		0	0.0	0.0	0.0	0.0	1	1	1	1	11000.0	13000.0						

663	crawler type agricultural machinery, straw chopper, feed harvester	1	1	371	1		1	1.0	1.0	2.3	3.0	1	1	1	1	27000.0	27000.0						

664	factory outlet other agricultural machinery & equipments mini tiller farm machinery equipment plow	1	30	372	1		1	4.7	12.0	4.7	4.8	1	1	1	1	53.0	54.0						

665	kubota 688q agriculture machinery combine harvester for rice and wheat	1	1	326	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6500.0	6500.0						

666	agriculture machine for harvesting engine 102 hp second hand rice combine harvester	1	1	373	1		0	3.0	2.0	4.3	5.0	1	1	1	1	8500.0	9000.0						

667	agricultural machinery micro tiller four-wheel drive loosening machine rotavator walking tractor mini power tiller cultivators	1	2	268	1		0	0.0	0.0	0.0	0.0	1	1	1	1	299.0	299.0						

668	farm cultivator multifunctional agricultural machinery farmland small gasoline ditching machine	1	10	374	1		0	5.0	2.0	5.0	5.0	1	1	1	1	800.0	900.0						

669	high productivity kubota mini rice harvester for paddy dc70 dc60 pro688q harvesting machine agricultural machinery in high quali	1	1	375	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8500.0	9000.0						

670	factory price energy-efficient agriculture machines from china	1	1	376	1		0	5.0	1.0	5.0	5.0	1	1	1	1	361.0	389.0						

671	agriculture machinery tractor hitch rotary 2 disc plough farm cultivator plow machine	1	1	157	1		0	5.0	2.0	5.0	5.0	1	1	1	1	260.0	330.0						

672	um gasoline 52cc 2stroke hand push tiller agricultural machine scarifier machine	1	200	377	1		0	4.9	6.0	4.8	4.8	1	1	1	1	108.0	168.0						

673	agricultural machinery equipment multifunction wheat rice threshing machine	1	2	378	1		0	4.7	11.0	4.5	4.2	1	1	1	1	31.08	241.0						

674	15hp garden hand electric garlic ridging cultivator tiller farming equipment agricultural machinery with rotary blade kenya	1	1	379	1		0	5.0	4.0	5.0	5.0	1	1	1	1	830.0	910.0						

675	40hp lovol 404-e tractor used agricultural machinery & equipment cheap agricultural machinery equipment used 4wd	1	1	219	1		0	4.6	14.0	4.5	4.7	1	1	1	1	5000.0	6000.0						

676	wholesale 16l 25 bar knapsack sprayer agriculture machine gasoline power sprayer dosing machine	1	10	252	1		4	4.2	9.0	4.3	4.3	1	1	1	1	56.25	58.5						

677	tractor farm /mini tractor with rotary tiller plow various agricultural machinery	1	1	165	1		2	4.3	8.0	4.5	4.6	1	1	1	1	1300.0	2500.0						

678	buy cheap high quality performance combine harvester agricultural machine for rice corn wheat /4 rows silage machine for sale	1	1	216	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7000.0	9500.0						

679	agricultural machinery 50hp mini diesel crawler tractor	1	1	152	1		5	4.5	12.0	4.4	4.5	1	1	1	1	1980.0	4980.0						

680	agricultural machinery & equipment 600 liter customized pto shaft for tractor 3-point sprayer	1	1	221	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1060.0	1160.0						

681	farm multipurpose agricultural machinery agricultural machines other agricultural machinery	1	1	171	1		0	4.1	65.0	4.4	4.4	1	1	1	1	230.0	538.0						

682	massey ferguson 4270 agricultural machinery / used 85hp mf4270 farm tractor available for sale	1	10	217	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	4500.0						

683	best cheap agriculture machinery combine harvester for rice and wheat rice harvester mini combine harvester for sale	1	1	155	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7300.0	7300.0						

684	agricultural machinery 170 gasoline mini power weeder diesel power tiller weeding and soil loosening and trenching machine	1	1	233	1		0	4.2	19.0	4.4	4.5	1	1	1	1	275.0	335.0						

685	tractor holland fiat 110-90 130-90 160-90 180-90 farm orchard compact tractor agricultural machinery 6 cylinders	1	1	270	1		0	5.0	4.0	5.0	5.0	1	1	1	1	3000.0	6000.0						

686	25hp small crawler tractor farm mini rotary tiller plow various agricultural machinery	1	1	380	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1399.0	1599.0						

687	combine harvester 4lz-5 combine harvester price used combine harvester agriculture machine	1	1	262	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7000.0	8000.0						

688	lutong 1404 tractor 140hp 4wd agricultural machinery for sales	1	1	381	1		0	0.0	0.0	0.0	0.0	1	1	1	1	17000.0	18000.0						

689	competitive factory hay small baler agricultural machinery	1	1	382	1		0	4.5	1.0	4.5	5.0	1	1	1	1	2200.0	2300.0						

690	manufacturers direct sale micro tiller machine agricultural farming equipment agricultural cultivator machine	1	1	267	1		0	4.7	4.0	4.9	5.0	1	1	1	1	688.0	785.0						

691	multi functional strawberry ditching cultivator agriculture machinery farm ridging making machine ridges machine	1	1	383	1		0	4.6	20.0	4.6	4.6	1	1	1	1	695.0	695.0						

692	agricultural machinery precision direct automatic sunflower cotton peanut maize bean seeder machine	1	1	385	1		0	5.0	1.0	5.0	5.0	1	1	1	1	800.0	1000.0						

693	used tractor massey ferguson xtra 1204 120hp 4wd wheel farm orchard compact tractor agricultural machinery mf290 mf385	1	1	386	1		0	0.0	0.0	0.0	0.0	1	1	1	1	900.0	1600.0						

694	two-drive small four-wheel tractor multi-functional furrow ploughing agricultural machinery	1	1	240	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2475.0	2614.0						

695	tractor agricultural machinery 100% customer praise reliable crawler tiller rotary cultivator crawler tractor agricultural	1	1	387	1	CE	0	4.4	76.0	4.3	4.3	1	1	1	1	3500.0	3500.0						

696	500hp agricultural machinery for sell / fendt 1050 vario tractor for sale	1	1	388	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4050.0	4050.0						

697	hot sale self propelled tractor mist blower pesticide boom sprayer agricultural machinery	1	1	42	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1021.0	1021.0						

698	35hp mini 4x4 farm tractor machine for farm use	1	1	5	1	CE	0	4.6	25.0	4.6	4.6	1	1	1	1	3600.0	4030.0						

699	d 90hp 100hp 110hp 120hp 130hp austria tractor for agricultural machinery manufacturer 4wd used fendt tractors for sale	1	1	169	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2200.0	3000.0						

700	agricultural machinery equipment 350 liter pesticide spray machine house spray	1	1	221	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1250.0	1410.0						

701	orchard 100l gasoline powered cart agricultural motor high-pressure electric power pump sprayers garden spray machine	1	1	268	1		0	0.0	0.0	0.0	0.0	1	1	1	1	242.0	242.0						

702	multifunctional big cylinder 4wheel drive 70hp 80hp 90hp ac cabin agricultural farm tractor	1	1	47	1	CE	0	4.4	13.0	4.3	4.3	1	1	1	1	7200.0	9054.0						

703	original mf 385 mf 390 4x4 tractor agricultural machinery massey fferguson tractor farm tractors for sale now	1	1	15	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2599.0	2750.0						

704	2 stroke knapsack pest control power mist blower agro sprayer agriculture machinery equipment	1	1	97	1		3	4.4	12.0	4.5	4.5	1	1	1	1	55.0	75.0						

705	farm watering rain gun agricultural sprayer sprinkler water hose reel irrigation machine drum system irrigator systems	1	1	79	1		0	3.3	4.0	3.8	4.2	1	1	1	1	1500.0	4700.0						

706	multi purpose tractors for agriculture used 180 200 220 260hp medium big large tractor	1	1	125	1		0	4.3	5.0	4.5	5.0	1	1	1	1	14000.0	18000.0						

707	lisa heavy duty disc plough 3 point hitch disc plow power tiller /tractor drive plowing machinery disc plow	1	1	161	1		2	3.6	2.0	3.2	3.0	1	1	1	1	175.0	220.0						

708	buy cheap price second hand fairly used quality john deer 6r agricultural tractor 8r combine harvesters for sale from usa	1	1	163	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5440.0	5440.0						

709	small agriculture machinery power tiller diesel motoblok	1	1	104	1		0	5.0	17.0	4.9	4.9	1	1	1	1	250.0	400.0						

710	factory outlet combined mixer and agricultural grass processing grain corn grinder animal livestock poultry chicken feed crusher	1	1	38	1		0	4.8	18.0	4.7	4.7	1	1	1	1	220.0	230.0						

711	2022 hot multi crop grain seed drill machine sesame rice wheat seed planter	1	1	166	1		1	4.2	16.0	4.2	4.1	1	1	1	1	640.0	640.0						

712	buy shop online cheap tractor with loader for sale used tractors for agriculture wheel tractor agricultural machinery equipment	1	1	112	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	5000.0						

713	new tractor 4x4 four-wheel tractors in new condition tractors for agriculture	1	1	389	1		0	0.0	0.0	0.0	0.0	1	1	1	1	14500.0	15000.0						

714	sprayers agriculture machinery equipment farm cultivator rotary tiller agricultural mini crawler tractor	1	1	251	1		2	4.6	188.0	4.6	4.5	1	1	1	1	5500.0	5500.0						

715	original massey ferguson mf 135 mf 185 mf 188 2wd tractor agricultural machinery massey ferguson tractor farm tractors for sale	1	1	126	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1300.0	1300.0						

716	wholesale 50hp 60hp 70hp 90hp 150hp agricultural machine equipment wheel farm tractor for sale	1	1	322	1		0	4.0	17.0	4.1	4.1	1	1	1	1	3000.0	3000.0						

717	chinese tractor marketing key high quality multipurpose mini power rotary tillage weeding machine tiller agriculture cultivator	1	1	225	1		0	4.7	28.0	4.6	4.4	1	1	1	1	380.0	380.0						

718	big promotion 10-300hp mini tractor pulling tractors micro chinese garden tractor attachments for agriculture for sale	1	1	168	1	CE	0	4.5	125.0	4.4	4.3	1	1	1	1	2599.0	2599.0						

719	used tractors kubota 4x4 farming machine agricultural tractor agricola used kubota tractor	1	1	145	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3344.4	4459.2						

720	agricultural machinery equipment ox drawn plow / animal drawn plow plough for sale	1	1	172	1		0	3.6	2.0	4.0	4.5	1	1	1	1	30.0	50.0						

721	harvester machine wheat rice combine harvesters mini small combine harvester	1	1	217	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	3000.0						

722	cheap products cost effective agricultural machinery equipment 4wd horsepower used kubota tractors kubota m7131 tractor	1	1	108	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3300.0	3400.0						

723	used farming tractors john deere 95hp 4x4 tractor agricultural machinery cheap farm tractor for sale	1	1	129	1		0	1.0	1.0	1.0	1.0	1	1	1	1	12500.0	12700.0						

724	mini agriculture machinery four-wheel drive compact orchard garden farm equipment tractor with ce small tractor	1	1	220	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1860.0	6176.0						

725	best sale farm cultivator agricultural machinery crawler tractor mini rotary tiller ridger gears tiller	1	1	229	1		0	4.9	23.0	4.9	4.8	1	1	1	1	1900.0	3000.0						

726	tractor popular agricultural products 180 -90 equipment machinery cheap 4*4 tractores agricolas	1	1	219	1		0	4.6	14.0	4.5	4.7	1	1	1	1	28500.0	28700.0						

727	agricultural machinery knapsack maize thresher corn thresher with diesel	1	1	170	1		0	4.8	6.0	4.6	4.6	1	1	1	1	2600.0	3200.0						

728	3zt-1.8 agricultural machinery cultivator with good price	1	1	208	1		0	4.5	8.0	4.7	4.8	1	1	1	1	199.0	199.0						

729	land universal 25hp epa engine agriculture tractors 4wd 4x4 90 100 120 140 160 180 hp aw farm tractor	1	1	218	1		0	5.0	4.0	5.0	5.0	1	1	1	1	2000.0	2100.0						

730	agricultural weeding and loosening machine small gasoline plough tiller wooden box new product 2020 provided red cultivator 45	1	1	116	1		0	4.9	31.0	4.9	5.0	1	1	1	1	145.0	285.0						

731	a light chain drive agricultural equipment tool mini rotary power tiller rototiller for 30-35 horsepower tractors used on a farm	1	3	134	1		0	0.0	0.0	0.0	0.0	1	1	1	1	385.0	416.0						

732	high quality agriculture 400 liter three-point hanging sprayer tractor mounted sprayer	1	1	115	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1361.0	1411.0						

733	agricultural machinery fully operational corn straw baler class 65 used farming equipment	1	4	270	1		0	5.0	4.0	5.0	5.0	1	1	1	1	3000.0	4500.0						

734	multi functional farm tractor agricultural machine shuttle farm tractor with implements	1	1	222	1		3	5.0	5.0	5.0	5.0	1	1	1	1	3000.0	5000.0						

735	hot sale agricultural machinery automatic mini forage alfalfa hay grass round bundler baler	1	1	233	1		0	4.2	19.0	4.4	4.5	1	1	1	1	1950.0	2650.0						

736	multi-gear operation with adjustable high and low speeds, high-quality agricultural machinery tractors, heavy-duty belt tractors	1	1	232	1		0	3.1	8.0	3.2	3.3	1	1	1	1	2600.0	3000.0						

737	small implements for compact tractor with front loader mini agriculture tractor front end loader 90hp attachments bucket chinese	1	1	236	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3999.0	9999.0						

738	4wheel used tractor new holland tt75 4wd agricultural machinery & equipment for farmland	1	1	223	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2463.0	2463.0						

739	agricultural machinery rotary tiller made in china with best quality	1	1	29	1		0	4.9	10.0	4.9	4.9	1	1	1	1	560.0	560.0						

740	fendt 210 vario agricultural machinery for sell	1	1	209	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	4000.0						

741	new john deeree hpx 615e gator 4wd w power box lift agricultural machinery & equipment	1	1	26	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	2500.0						

742	hotoka 52cc gasoline power tiller crawler mini garden cultivator agriculture machine walking tractor rotary tiller for sale	1	2	20	1	CE	2	4.8	40.0	4.9	4.9	1	1	1	1	59.0	80.0						

743	small agriculture machinery film mulching machine	1	1	211	1		0	0.0	0.0	0.0	0.0	1	1	1	1	180.0	278.0						

744	diesel power 8hp mini walking tractors agricultural machine	1	1	18	1	CE	0	4.5	14.0	4.5	4.5	1	1	1	1	480.0	520.0						

745	best sales hand small agricultural machinery&equipment tractors for ditching weeding tiller and tilling cultivators	1	1	212	1		0	4.5	2.0	4.8	5.0	1	1	1	1	230.0	255.0						

746	agricultural machine tractor mounted plastic mulch laying machine	1	2	224	1		0	4.5	2.0	4.5	4.5	1	1	1	1	500.0	700.0						

747	weeding grow kit other agricultural machinery & equipment weeder	1	1	98	1		0	5.0	3.0	5.0	5.0	1	1	1	1	2150.0	2150.0						

748	second hand agriculture 130 hp tractors s1304-c with loader and implement agricultural machinery	1	1	162	1		0	0.0	0.0	0.0	0.0	1	1	1	1	16000.0	30000.0						

749	household small compact mini diesel rotary tiller farming machine ride type crawler agricultural machinery	1	1	225	1		0	4.7	28.0	4.6	4.4	1	1	1	1	2099.0	2139.0						

750	agricultural machinery farm irrigation systems center pivot watering machine	1	1	390	1		0	4.9	40.0	4.8	4.8	1	1	1	1	2000.0	2050.0						

751	high efficiency agriculture machine rice and wheat thresher,rice paddy thresher machine,many uses of thresher	1	1	391	1		0	5.0	1.0	5.0	5.0	1	1	1	1	420.0	480.0						

752	agriculture machinery tractor corn maize harvester machine/farm use grass maize harvester/forage harvester	1	1	289	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2970.0	2980.0						

753	multifunctional garden agriculture farm machine 4 stroke 52cc hand types mini rotary gasoline power tiller	1	1	392	1		0	0.0	0.0	0.0	0.0	1	1	1	1	139.0	179.0						

754	12hp the most compact 4-wheel tractors manufacturer agricultural machine	1	1	393	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1352.0	1352.0						

755	agricultural machinery and equipment grain harvesters	1	1	394	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1000.0	1050.0						

756	tractor parts massey ferguson plough africa market plough disc plow ploughing machine agricultural machinery agro machine	1	5	133	1		0	5.0	2.0	5.0	5.0	1	1	1	1	780.0	850.0						

757	agricultural machinery automatic corn silage packing machine silage baler machine for sale	1	1	395	1		0	4.8	5.0	4.6	4.8	1	1	1	1	1999.0	2490.0						

758	sand dewatering hydrocyclone for sale, agricultural machinery for animal dung separator, solid liquid separator	1	1	324	1		0	3.0	2.0	3.0	3.0	1	1	1	1	900.0	1200.0						

759	agricultural machinery equipment diesel cultivator motocultor 2 wheel gasoline power tiller 6hp walking tractor/cultivators	1	1	396	1		0	4.2	4.0	4.4	4.5	1	1	1	1	350.0	380.0						

760	used/second hand/new tractor mf554 4x4wd farming equipment agricultural machinery with front loader backhoe 55hp	1	1	397	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6000.0	6500.0						

761	japan kubotapro758q forage rice and peanut combined harvester machine berry wheat harvester agricultural machine	1	1	398	1		0	5.0	1.0	5.0	5.0	1	1	1	1	13500.0	14000.0						

762	cambodia tractor alemania farm tractor agricultural machine buy tractor from china	1	1	222	1		3	5.0	5.0	5.0	5.0	1	1	1	1	3000.0	5000.0						

763	12hp mini farm tractor yto wheel tractor agricultural machine	1	1	156	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1299.0	1299.0						

764	agriculture machine used tractor mounted 3-point rotary tiller tools heavy duty rotary cultivator rotary tiller rototiller	1	1	236	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0						

765	agricultural machinery and equipment crawler rotary tillers garden cultivators and cultivators agricultural tractors	1	1	399	1		0	5.0	3.0	5.0	5.0	1	1	1	1	3980.0	4080.0						

766	xptool agricultural machinery equipment garden mini cultivators mini power tiller machine	1	40	400	1		0	4.9	9.0	4.7	4.3	1	1	1	1	215.0	226.0						

767	rolande chinese micro-tiller desiel/gasoline power tiller agricultural machinery for sale	1	50	401	1		0	5.0	2.0	5.0	5.0	1	1	1	1	580.0	580.0						

768	agricultural machinery multi-function grain corn peeler corn maize peeling sheller thresher machine for millet sorghum 3 ton/h	1	1	402	1		0	5.0	2.0	5.0	5.0	1	1	1	1	119.0	179.0						

769	agricultural machinery feed processing machinery poultry cattle pig sheep chicken animal feed pellet mill machine	1	1	403	1	CE	1	4.7	17.0	4.4	4.4	1	1	1	1	400.0	450.0						

770	high quality 45tpd rice milling/agricultural machinery equipment/45tpd rice parboiling machine	1	1	404	1		0	0.0	0.0	0.0	0.0	1	1	1	1	300000.0	330000.0						

771	pig feed grinder agricultural machinery	1	1	405	1		0	0.0	0.0	0.0	0.0	1	1	1	1	60.0	65.0						

772	agriculture machinery seeders planting machine lettuce drop seeder	1	10	300	1		0	4.2	30.0	4.4	4.6	1	1	1	1	43.0	63.05						

773	nfy-802 china good quality rubber crawler tractor agricultural machinery and equipment	1	1	406	1		0	0.0	0.0	0.0	0.0	1	1	1	1	14900.0	14900.0						

774	land leveling high-efficiency 6m laser land grader cultivator machine more agricultural machines	1	1	79	1		0	5.0	1.0	5.0	5.0	1	1	1	1	21170.0	28228.0						

775	best sale high performance 12 hp electric walking tractor agricultural machine	1	1	407	1		0	0.0	0.0	0.0	0.0	1	1	1	1	600.0	690.0						

776	agriculture machinery combine harvester for rice and wheat cheap combine harvester available	1	1	408	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0						

777	new designed agricultural machinery and equipment gasoline tiller multi cultivator power tillers	1	30	409	1		0	0.0	0.0	0.0	0.0	1	1	1	1	195.0	197.0						

778	high quality classic farm pesticide spraying tractor agriculture machine	1	1	410	1		0	0.0	0.0	0.0	0.0	1	1	1	1	14000.0	15000.0						

779	newly designed high-quality agricultural machinery and equipment manual disc units	1	1	411	1		0	0.0	0.0	0.0	0.0	1	1	1	1	54.5	110.0						

780	compact farm 4wd tractor agricultural machine 25hp 30hp 35hp 40hp 50hp lt504	1	1	412	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7500.0	8000.0						

781	agricultural machine unmanned vineyard sprayer 500l large volume	1	1	413	1		0	5.0	6.0	5.0	5.0	1	1	1	1	5899.0	8099.0						

782	kubota bx2380 tractor agricultural machinery	1	1	415	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0						

783	70hp farm tractors agriculture 4 stroke tractor agricultural machinery	1	1	416	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4277.0	4277.0						

784	new 140hp farm diesel tractor 4wd agricultural machinery sale at competitive chinese tractors prices	1	1	327	1	CE	0	0.0	0.0	0.0	0.0	1	1	1	1	21185.0	21785.0						

785	2024 top brand agricultural machinery 4 rows 100hp mini corn potato combine harvester machine af108 with attachments	1	1	417	1		0	0.0	0.0	0.0	0.0	1	1	1	1	15000.0	20000.0						

786	land universal crawler tractor farm orchard paddy field with rotary tiller plow various agricultural machinery	1	1	218	1		0	5.0	4.0	5.0	5.0	1	1	1	1	2000.0	2100.0						

787	lovol904 agriculture machinery 90hp with cabin tractors for agriculture used tractores 4x4 four-wheel drive tractor	1	1	230	1		0	0.0	0.0	0.0	0.0	1	1	1	1	20250.0	20250.0						

788	lutian agricultural machinery 4wd 80hp 90hp 100hp mini tractor with canopy/cabin	1	1	299	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4300.0	5000.0						

789	agricultural machinery grass cutting feed corn silage making chopper crusher feed processing chaff cutter machine	1	1	418	1		0	5.0	4.0	5.0	5.0	1	1	1	1	170.0	185.0						

790	agricultural machinery high-power weeding machine gasoline-powered lawn mower trimming trees pumping loosening soil ditching	1	1	419	1		0	0.0	0.0	0.0	0.0	1	1	1	1	109.0	109.0						

791	gasoline agricultural machinery 4kw farm equipment/mini rotary tiller, high quality agricultural machinery	1	1	197	1		0	5.0	6.0	5.0	5.0	1	1	1	1	325.3	357.8						

792	agriculture machinery three wheel tractor agricultural sprayer price	1	1	182	1		0	4.2	5.0	4.3	4.6	1	1	1	1	800.0	900.0						

793	agricultural machinery gasoline machine seeder multifunctional corn peanut soybean precision seeder wheat millet fertiliser	1	1	420	1		3	4.5	31.0	4.6	4.6	1	1	1	1	46.0	48.0						

794	agricultural machinery farm equipment crawler type diesel gasoline power hand-held chain track cultivator small tractor plow	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	226.8	510.3						

795	second hand tractors lovol tractors m554-b 55hp for sale cheap farm tractors agricultural machinery	1	1	164	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2300.0	2300.0						

796	chinese mini 22 hp farm power tiller walking tractors agricultural machinery with farm lawnmower equipment kenya	1	1	379	1		0	5.0	4.0	5.0	5.0	1	1	1	1	400.0	650.0						

797	factory direct sales 2024 new agricultural machinery for sale at low prices disc harrows plows	1	1	157	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1700.0	1900.0						

798	affordable 4wd massey ferguson 290 tractor 80 hp59.7 kw / massey ferguson 120hp with farm equipment agricultural machinery	1	1	216	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	6000.0						

799	world 118hp agriculture machinery combine harvester for rice and wheat	1	1	326	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6914.0	6914.0						

800	hot selling durable agricultural machinery and equipment multi function disc plough for tractors at cheap prices	1	1	155	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2006.64	2229.6						

801	30hp 4x4 farm mini tractor with front loader 4 in 1 bucket agricultural machinery	1	1	152	1		8	4.5	12.0	4.4	4.5	1	1	1	1	3500.0	6990.0						

802	agricultural machinery mini crawler cultivator made in china farm ploughing machine rotary power tiller	1	1	158	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1690.0	1690.0						

803	agriculture machinery 5300 combine harvester/ fairly used agriculture machinery combine harvester for sale to usa europe	1	1	145	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3500.0	5000.0						

804	best quality cheap massey ferguson 385tractors / massey ferguson 385 agricultural machinery for sale austria	1	1	15	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	2500.0						

805	orchard self propelled sprayer agricultural machine for farm spraying 200 liter fruit tree sprayer	1	1	221	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1380.0	1430.0						

806	agricultural machinery hot sale factory direct price 540hp four wheel farm tractor massey ferguson/massey tractors	1	1	386	1		0	0.0	0.0	0.0	0.0	1	1	1	1	900.0	1600.0						

807	used balers massey ferguson 1840 claas 65 agricultural machinery farm equipment	1	1	270	1		0	5.0	4.0	5.0	5.0	1	1	1	1	9000.0	9000.0						

808	skid steer rock picker stone removal machine hydraulic powered rock debris picker	1	1	421	1		0	3.2	4.0	2.7	1.7	1	1	1	1	1890.0	2100.0						

809	high quality free shipping chinese 45hp small tractor agricola for farm agriculture machine 35 40 50 hp tractor mini 4x4 4wd	1	1	220	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1600.0	2500.0						

810	high quality hot sale tractors compact chinese small mini farm tractor mini 4x4 agricultural machinery	1	1	5	1	CE	0	4.6	25.0	4.6	4.6	1	1	1	1	3950.0	4000.0						

811	hot selling agricultural machinery convenient and fast weeding and hay baling machine small square baler mf1840	1	1	154	1		0	0.0	0.0	0.0	0.0	1	1	1	1	20000.0	20000.0						

812	economical and affordable agriculture machine used fiat 110-90 in stock for sale	1	1	219	1		0	4.6	14.0	4.5	4.7	1	1	1	1	13000.0	13500.0						

813	new style animal feed machinery livestock feed agricultural straw feed crusher machine manufactured in china	1	1	38	1		1	4.8	18.0	4.7	4.7	1	1	1	1	220.0	230.0						

814	yto lx904 cultivators tiller farm compact powerful chinese manufacturer agricultural machine	1	1	162	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6000.0	10000.0						

815	best supplies agriculture machinery combine harvester for rice and wheat cheap combine harvester available	1	1000	169	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5500.0	5500.0						

816	high efficiency sugarcane planting machine easy to operator sugarcane seeder professional sugarcane agricultural machine	1	1	153	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4800.0	5000.0						

817	tractor gps land leveling machinery industry equipment farm used agricultural machinery	1	1	79	1		0	5.0	1.0	5.0	5.0	1	1	1	1	1500.0	2300.0						

818	hot selling small ploughing machine mini cultivator tiller agriculture machinery	1	1	42	1		0	5.0	2.0	5.0	5.0	1	1	1	1	353.0	353.0						

819	professional soybean harvester manufacturer price brazil hot sale soybean combine harvesting agriculture machine	1	1	389	1		0	0.0	0.0	0.0	0.0	1	1	1	1	18200.0	18700.0						

820	agriculture machinery vegetable seeder tractor mounted high precision vegetable seeder machine	1	1	160	1		0	4.8	3.0	4.7	4.6	1	1	1	1	1250.0	1300.0						

821	new tractor 18hp 4wd wheel farm orchard compact tractor agricultural machinery	1	1	165	1		0	4.3	8.0	4.5	4.6	1	1	1	1	1300.0	2500.0						

822	best quality mahindra 225 2wd 4wd tractor farm tractors agricultural machinery	1	1	414	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1800.0	3500.0						

823	agricultural machinery mini cultivator/rotary gasoline power cultivator/small cultivation equipment rotary cultivator	1	1	268	1		0	0.0	0.0	0.0	0.0	1	1	1	1	88.0	110.0						

824	new 4wd wheel diesel tractor chinese agricultural machinery with bearing plc-for farms	1	1	327	1	CE	0	0.0	0.0	0.0	0.0	1	1	1	1	27610.0	28210.0						

825	land universal china agricultural machinery 4 wheeled tractor cheap 4x4 farming tractors compact for sale	1	1	218	1		0	5.0	4.0	5.0	5.0	1	1	1	1	2000.0	2100.0						

826	two wheeled diesel engines, small cultivators, handheld tractors, agricultural machinery	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	455.0	455.0						

827	wholesale price high quality industrial/agricultural machinery automatic vibrating pea cleaning machine stainless steel	1	1	422	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2880.0	3280.0						

828	agriculture products cultivators mini farm walking tractor two wheel tractor ploughing machine agricultural machine	1	1	43	1		0	0.0	0.0	0.0	0.0	1	1	1	1	340.0	400.0						

829	cheap agriculture machinery massey ferguson 9560 combine harvester/ fairly used agriculture machinery combine harvester 9560	1	1	181	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9000.0	13000.0						

830	12hp the most multi-function tractors manufacturer agricultural machine and diesel motors	1	15	393	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1352.0	1352.0						

831	new design machine sprayer knapsack sprayer agriculture machine insecticide spray machine for insects	1	1	161	1		0	3.6	2.0	3.2	3.0	1	1	1	1	79.0	91.0						

832	high efficiency original used massey ferguson mf 231s tractor agricultural machinery	1	1	55	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	5000.0						

833	high performance top sale compact farm 4*4 tractor agricultural machine 120hp	1	1	230	1		0	0.0	0.0	0.0	0.0	1	1	1	1	11042.0	11042.0						

834	case ih tractor premium quality original case ih agricultural machinery for sale	1	1	48	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5016.6	5574.0						

835	agricultural machinery corn fertilization seeder for tractor	1	1	156	1		0	5.0	2.0	5.0	5.0	1	1	1	1	559.0	599.0						

836	70hp 704 farming tractors agriculture machinery in tavol	1	1	125	1		0	4.3	5.0	4.5	5.0	1	1	1	1	6500.0	6600.0						

837	fairly used agriculture machinery combine harvester new-holland cr9060 for rice and wheat cheap combine harvester from france	1	1	164	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7500.0	7500.0						

838	heavy duty plough agricultural machine	1	1	224	1		0	5.0	1.0	5.0	5.0	1	1	1	1	750.0	758.0						

839	wheat maize beans sesame rice seed cleaner agricultural machinery	1	1	101	1		0	5.0	3.0	5.0	5.0	1	1	1	1	1000.0	5000.0						

840	multi functional agricultural machinery mini 4 stroke gasoline garden rotary tiller machine cultivator soil cultivating machine	1	1	423	1		2	4.9	65.0	4.9	4.9	1	1	1	1	120.0	148.0						

841	hot sale agricultural machine used for farmly ditching machine 1ks-35	1	10	424	1		0	5.0	5.0	5.0	5.0	1	1	1	1	826.0	829.0						

842	agriculture machine with cultivator ridger and plastic mulch layering applicaror machine	1	1	132	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0						

843	small agriculture machinery motocultor mini plough machine	1	1	104	1		0	5.0	17.0	4.9	4.9	1	1	1	1	250.0	400.0						

844	other agricultural machines chain trencher pipe digger machine for sale at reasonable price	1	1	380	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1500.0	1650.0						

845	th80-2 unmanned helicopter remote control agriculture sprayer farm machinery	1	1	425	1		0	0.0	0.0	0.0	0.0	1	1	1	1	16000.0	25000.0						

846	agricultural machinery equipment 60hp 4wd farm tractor multifunctional agriculture machinery equip for sale	1	1	5	1	CE	0	4.6	25.0	4.6	4.6	1	1	1	1	4600.0	4656.0						

847	d 90hp 100hp 110hp 120hp 130hp france tractor for agricultural machinery manufacturer 4wd used fendt tractors for sale	1	1	426	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	4000.0						

848	agriculture spray fumigation machine a30 big drone sprayer uav drone	1	1	427	1	FCC,CE	3	5.0	8.0	5.0	5.0	1	1	1	1	5600.0	5600.0						

849	farm machinery used agricultural machinery & equipment agricultural machinery	1	1	171	1		0	4.1	65.0	4.4	4.5	1	1	1	1	230.0	540.0						

850	2021 hot sell luckystar rice harvester farm machine whole-feed/full-feed rice combine harvester agriculture machine	1	2	428	1		0	5.0	17.0	5.0	5.0	1	1	1	1	12700.0	12700.0						

851	hot sle good deal great condition 2022 front farm tractors 5115m agricultural machinery for sale	1	1	429	1		0	0.0	0.0	0.0	0.0	1	1	1	1	33500.0	34000.0						

852	rice cutter harvester machine modern agricultural machinery harvester machine agricultural	1	1	98	1		0	5.0	3.0	5.0	5.0	1	1	1	1	1850.0	1850.0						

853	2wd mini tractor agricultural machinery with grass cutter	1	1	302	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1100.0	2200.0						

854	small farm tractors with rubber tracks crawler tractor agricultural machinery 25hp mini crawler tractor for sale	1	1	166	1		2	4.2	16.0	4.2	4.1	1	1	1	1	1400.0	1400.0						

855	500kg per hour mini parboiled electric motor portable rice husking mill agriculture machine	1	1	430	1		0	0.0	0.0	0.0	0.0	1	1	1	1	150.0	170.0						

856	tractor agricultural machinery 280hp tractors for agriculture	1	1	431	1		0	5.0	1.0	5.0	5.0	1	1	1	1	45000.0	65000.0						

857	small tractor arable disc plow manual agricultural machinery	1	1	160	1		0	4.8	4.0	4.7	4.7	1	1	1	1	530.0	680.0						

858	cheap price agricultural equipment john deer x950r lawn mower tractor mini garden tractor john deer agricultural machinery	1	4	432	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1390.0	1390.0						

859	anon agricultural machinery and equipment tractor farming mini garden tractors	1	1	114	1		0	5.0	5.0	4.7	4.2	1	1	1	1	500.0	1500.0						

860	low moq china manufacturer mini electric agricultural machinery grass cutter machine	1	1	433	1		0	5.0	2.0	5.0	5.0	1	1	1	1	1485.0	1485.0						

861	purchase excellent condition case ih tractor agricultural machinery / 110hp case ih tractor available at modaret prices	1	1	108	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2200.0	2650.0						

862	reasonable price farm plow land sugarcane cassava ground cultivators mini hand held small agricultural plough machine	1	1	102	1		51	4.9	39.0	4.9	4.9	1	1	1	1	99.0	99.0						

863	palm oil plantation tractor 4x4 all road farm small agriculture machinery	1	2	434	1		0	0.0	0.0	0.0	0.0	1	1	1	1	18000.0	19500.0						

864	agriculture machine grass cutter, industrial grass cutting machine, straw cutting machine	1	1	435	1		0	3.0	3.0	3.4	3.6	1	1	1	1	300.0	300.0						

865	professional supplier 4wd farm tractor 100hp 110hp china traktor other farm machines agricultural machinery	1	1	100	1		0	0.0	0.0	0.0	0.0	1	1	1	1	15000.0	17000.0						

866	agricultural machinery manufacturers	1	3	134	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1470.0	1507.0						

867	new design of lawn mower/grass cutter agricultural machinery	1	1	436	1		0	4.8	10.0	4.6	4.5	1	1	1	1	500.0	500.0						

868	20hp rome plough disc garden loader with plough agriculture machinery equipment plough walking tractor plow the field trench	1	1	158	1		0	5.0	3.0	5.0	5.0	1	1	1	1	829.99	849.99						

869	china new agricultural machines with names and uses	1	50	437	1		0	0.0	0.0	0.0	0.0	1	1	1	1	68.0	99.8						

870	agriculture machine ripper for tractor	1	1	438	1		0	0.0	0.0	0.0	0.0	1	1	1	1	300.0	700.0						

871	automatic 5 rows gasoline engine garlic planting sowing machine garlic planter machinery electric agriculture machinery	1	1	439	1		0	4.7	46.0	4.7	4.6	1	1	1	1	328.0	328.0						

872	operating walk behind mini skid steer loader small agriculture machinery	1	5	440	1		0	4.4	5.0	4.8	5.0	1	1	1	1	8000.0	8000.0						

873	agriculture machinery farm ridging machine, ridger disc plough tractor for sale	1	1	441	1		0	0.0	0.0	0.0	0.0	1	1	1	1	100.0	900.0						

874	machinery > agricultural machinery & equipment > cultivators agricultural machinery tractor price farm machineres	1	1	442	1		0	0.0	0.0	0.0	0.0	1	1	1	1	300.0	1000.0						

875	excavator hydraulic grass trimmer hedge trimmer / heavy duty tractor mulcher lawn mower for agricultural machine implement	1	5	443	1	CE	0	4.7	25.0	4.6	4.6	1	1	1	1	605.0	640.0						

876	chinese famous brand xr730 farming agricultural machinery corn rice combined harvester machine on hot sale	1	1	290	1		0	5.0	19.0	5.0	5.0	1	1	1	1	25000.0	38000.0						

877	k-maxpower 15hp highly productive chain saw ditching agricultural trencher machine	1	1	444	1		0	4.8	23.0	4.8	4.6	1	1	1	1	858.0	1155.0						

878	earthing moving machinery new 1.5t fronted wheel agricultural telescopic loader mini loaders	1	1	445	1		0	5.0	13.0	4.9	5.0	1	1	1	1	6000.0	7000.0						

879	tuv ce certificate k-maxpower 7hp max depth 450mm epa gasoline powered mini farm chain trencher machine	1	1	444	1	CE	0	4.8	23.0	4.8	4.6	1	1	1	1	775.0	975.0						

880	complete feed pellet line chinese factory aqua rabbit making tractored powered mill feed pellet machine	1	1	403	1	CE	0	4.7	17.0	4.4	4.4	1	1	1	1	700.0	700.0						

881	for sale small portable hydraulic tractor mounted mine water well drilling rigs machine	1	1	446	1		0	5.0	1.0	5.0	5.0	1	1	1	1	6800.0	7500.0						

882	high efficiency 60l hemp grow farm greenhouse farm greenhouse dehumidifier for plants	1	10	447	1		0	5.0	1.0	5.0	5.0	1	1	1	1	240.0	300.0						

883	low rpm ac helical worm robot arm tiller gearbox	1	1	448	1		0	5.0	7.0	5.0	5.0	1	1	1	1	900.0	1000.0						

884	hot sale tractor ce new 180hp farm tractor 4wd agricultural machinery for sale with air conditinal cabin	1	1	96	1	CE	2	4.4	108.0	4.4	4.3	1	1	1	1	980.0	980.0						

885	hot sales 2 stroke gasoline engine agriculture spray machine/tu26 knapsack power sprayer	1	1	449	1		8	4.3	70.0	4.3	4.3	1	1	1	1	59.0	59.0						

886	china cheap 25hp 30hp 40hp 50hp small tractors mini 4x4 farming machinery agricultural	1	1	450	1	CE	0	4.6	71.0	4.5	4.5	1	1	1	1	3999.0	4500.0						

887	high quality 50hp china factory price agricultural equipment farm agriculture machinery & equip tractor cheap price	1	1	294	1	CE	0	5.0	30.0	5.0	5.0	1	1	1	1	5500.0	5710.0						

888	best quality agricultural machinery equipment wholesale agriculture leveling red laser machine at affordable price	1	5	451	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5200.0	5200.0						

889	engine multifunctional provided agricultural farm machinery moto cultivator mini land cultivation machine 4 stroke 33 1year	1	1	232	1		0	3.1	8.0	3.2	3.3	1	1	1	1	139.0	159.0						

890	rice and corn milling machines agricultural machinery equipment dustless self priming maize crushing grinder	1	10	452	1		0	4.4	51.0	4.4	4.4	1	1	1	1	210.0	215.0						

891	joy electric self-propelled weeding and cultivating tractor turns soil and ditches multifunctional agricultural machine	1	2	453	1		5	4.6	71.0	4.6	4.6	1	1	1	1	125.0	129.0						

892	seed seedling planting machine for agricultural machinery plant seedling machine price small vegetables adjustable transplanter	1	1	213	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4400.0	4600.0						

893	2023 new chinese big farm tractors qln-1504 150hp tractor agriculture machinery with yto diesel engine for sale in peru	1	1	13	1	CE	0	5.0	8.0	5.0	5.0	1	1	1	1	15000.0	16000.0						

894	5tf-45 corn sheller high quality agricultural corn sheller farm farm equipment professional agricultural machinery and equipment	1	1	208	1		0	4.5	8.0	4.7	4.8	1	1	1	1	320.68	400.0						

895	agricultural machinery 4wd 25hp to 180hp mini tractor with cabin multifunction mini tractor	1	2	96	1		0	4.4	108.0	4.4	4.3	1	1	1	1	980.0	980.0						

896	3 rows latest agriculture machine 2 stroke paddy power weeder with high effciency	1	1	97	1		0	4.4	12.0	4.5	4.5	1	1	1	1	520.0	545.0						

897	agricultural machinery equipment low price seed wheat length grader paddy rice cleaning machine	1	1	101	1		0	5.0	3.0	5.0	5.0	1	1	1	1	5200.0	5300.0						

898	power tiller diesel engine agricultural machinery parts wheel power tiller weeding machine agriculture machine	1	1	98	1		2	5.0	3.0	5.0	5.0	1	1	1	1	650.0	650.0						

899	farming equipment agricultural machinery power tiller machine	1	1	104	1		0	5.0	17.0	4.9	4.9	1	1	1	1	425.0	465.0						

900	massey ferguson 240 tractor agricultural machinery / used 85hp farm tractor	1	1	106	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3500.0						

901	hot sale latest agriculture machine of manual seeder/seed planter/ seeder/grain seeding machine	1	1	109	1		6	4.1	40.0	4.2	4.3	1	1	1	1	9.0	11.0						

902	farming sprayer water pump orchard sprayer hand push agriculture machinery	1	1	110	1		0	0.0	0.0	0.0	0.0	1	1	1	1	840.0	895.0						

903	kubota tractor agricultural machinery for sale	1	1	37	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	2500.0						

904	anon best sale mini combine harvester prices multifunctional agricultural machines	1	1	114	1		0	5.0	5.0	4.7	4.2	1	1	1	1	2000.0	4000.0						

905	new 50 hp 4-wheel farm factory tractor mini agriculture machinery with 4wd for retail home use featuring a new engine motor gear	1	1	116	1		0	4.9	31.0	4.9	5.0	1	1	1	1	4500.0	4800.0						

906	used claas 630 rexion agriculture machinery combine harvester for rice and wheat cheap combine harvester from germany	1	1	22	1		0	0.0	0.0	0.0	0.0	1	1	1	1	15700.0	18500.0						

907	high quality agricultural machinery 15hp motor powered wood chipper machine, chipper shredder	1	1	107	1		0	4.8	8.0	4.7	4.5	1	1	1	1	410.0	610.0						

908	tractor manufacturer garden tractor 130hp 140hp 150hp agricultural machines buy farm tractor	1	1	19	1		0	4.8	9.0	4.7	4.6	1	1	1	1	16900.0	17200.0						

909	made in china agricultural machinery rotary tiller for tractor	1	1	113	1		1	4.2	5.0	4.3	4.8	1	1	1	1	1600.0	1800.0						

910	meiqi 190-4 gasoline mini power tiller tractor garden agriculture machine	1	65	255	1		0	5.0	1.0	5.0	5.0	1	1	1	1	290.0	350.0						

911	high performance kubota combine harvester dc-105x cabin (2350 l) agricultural machinery harvester wheat cutter machine	1	1	121	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0						

912	agricultural machinery accessories rotary farm cultivator garden tillers and cultivator rotary tiller	1	1	119	1		1	4.8	12.0	4.8	4.8	1	1	1	1	450.0	550.0						

913	2023 new collection construction equipment front end loader use agricultural machinery at affordable price	1	1	123	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2090.0	2682.0						

914	high productivity harvester agriculture machinery combine harvester for corn and maize combine harvester	1	1	130	1		0	5.0	1.0	5.0	5.0	1	1	1	1	32500.0	33000.0						

915	agriculture groundnut picking machine combine peanut harvester to harvesting peanut	1	1	103	1		0	4.7	3.0	4.8	4.6	1	1	1	1	13980.0	14840.0						

916	chinese factory directly supply agricultural machine /agricultural equipment/agricultural farm tractor for sale	1	1	124	1		0	5.0	6.0	5.0	5.0	1	1	1	1	1500.0	1700.0						

917	used tractor holland fiat 110-90 130-90 160-90 180-90 farm orchard compact tractor agricultural machinery 6 cylinders fiat 110-	1	1	120	1		1	4.8	36.0	4.8	4.7	1	1	1	1	12500.0	12800.0						

918	farm machinery equipment agricultural hoe tractor cultivator rotary display agriculture machine	1	1	118	1		0	5.0	11.0	5.0	5.0	1	1	1	1	149.0	459.0						

919	crawler tractor farm orchard paddy field mini crawler tractor with rotary tiller plow various agricultural machinery	1	1	132	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	1190.0						

920	agriculture machinery 3 point disc plough mounted with farm tractor rotary tiller power harrow	1	1	115	1	CE	7	5.0	2.0	5.0	5.0	1	1	1	1	200.0	200.0						

921	multifunctionality in agriculture machines rotary tiller small ditching machines farming weeder	1	1	182	1		0	4.2	5.0	4.3	4.6	1	1	1	1	300.0	330.0						

922	buy original ma ssey fer guson 275, mf 375 mf 385 mf 390 4x4 tractor agricultural machinery and get free accessories	1	1	164	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	3000.0						

923	cheap price agriculture machinery claas lexion 5300 combine harvester/ fairly used agriculture machinery combine harvester	1	1	126	1		0	0.0	0.0	0.0	0.0	1	1	1	1	33000.0	33000.0						

924	kubota 688q rice combine harvester agricultural machinery	1	1	326	1		0	0.0	0.0	0.0	0.0	1	1	1	1	7500.0	7500.0						

925	agricultural machine 50hp garden tractor 4wd with high quality for sale	1	1	47	1	CE	0	4.4	13.0	4.3	4.3	1	1	1	1	2699.0	3499.0						

926	agriculture machinery hand tractor hitch trailer machine on sale	1	1	157	1		1	5.0	2.0	5.0	5.0	1	1	1	1	260.0	330.0						

927	tavol supplier 50hp tractor farming tractors 60hp 70hp 80hp 90hp 100hp 4x4 tractor agricultural machinery	1	1	125	1	CE	0	4.3	5.0	4.5	5.0	1	1	1	1	7900.0	8600.0						

928	zongshen high quality gasoline rotary tiller new agricultural machinery elderly farm orchard functions soil loosening weeding	1	1	151	1		0	0.0	0.0	0.0	0.0	1	1	1	1	184.33	206.02						

929	small rice transplanter agricultural machinery made in japan products	1	1	36	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5000.0	15000.0						

930	agricultural machinery, tractor equipment, straw crushing and returning machine	1	1	14	1		0	4.8	124.0	4.7	4.7	1	1	1	1	660.0	660.0						

931	2 wheel walking tractor walking behind two wheel tractor agriculture machine	1	1	172	1		0	3.6	2.0	4.0	4.5	1	1	1	1	450.0	520.0						

932	we are best suppliers of premium quality massey ferguson tractor 385 agricultural machine available for sale and ready to ship	1	1	216	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2700.0						

933	high quality 80hp 25-30 hp farm farming equipment agricultural tractor 4wd machinery with front end loader	1	1	131	1		0	5.0	17.0	5.0	5.0	1	1	1	1	4150.0	4200.0						

934	factory 80hp farm tractor traktor mini tractor 4*4 agriculture machinery with attachments	1	1	152	1		1	4.5	12.0	4.4	4.5	1	1	1	1	7980.0	8880.0						

935	hot selling durable agricultural machinery 2-6 row corn seeder soybean/maize seeder/ 4 row corn planter with fertilizer in stock	1	1	155	1		0	0.0	0.0	0.0	0.0	1	1	1	1	800.0	1200.0						

936	high efficiency agriculture machinery 2600 rpm rated and 3 cylinders liquid cooled engine 27hp b2741 kubota tractor	1	1	454	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6200.0	6500.0						

937	case ih 115u pro farmall tractor agricultural machinery	1	1	62	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0						

938	oem rechargeable portable garden lithium battery powered electric knapsack boom sprayer agricultural machinery	1	100	455	1		0	4.7	3.0	4.9	5.0	1	1	1	1	30.0	32.0						

939	knapsack power sprayer agricultural machinery 768 fumigadoras agricolas	1	50	456	1		0	5.0	6.0	5.0	5.0	1	1	1	1	45.0	55.0						

940	agricultural machinery cattle goat grass cutting straw silage chaff cutter animal feed making machine for farms	1	20	457	1		0	4.7	18.0	4.7	4.8	1	1	1	1	186.5	206.5						

941	running 4wd kubota tractor m9540 60hp 75hp 80hp 120hp farm tractor agricultural machinery available for sale..	1	1	458	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1300.0	1300.0						

942	ouchen high quality 180 eggs fully automatic roller hatchet agricultural machinery & equipment for sale	1	1	459	1		0	5.0	1.0	5.0	5.0	1	1	1	1	125.0	175.0						

943	compact 4wd diesel tractor de granja 4x4 50hp 8+8 gears hydraulic output stage 5 farm 50hp tractor agricultural machine	1	1	460	1		0	0.0	0.0	0.0	0.0	1	1	1	1	420.0	450.0						

944	110hp 100hp 120hp mini farm tractor agricultural machinery & equipment for agriculture used with backhoe loader power tiller	1	1	461	1		0	5.0	1.0	5.0	5.0	1	1	1	1	3780.0	5980.0						

945	zeyi factory 1-6 rows hand push vegetable seeder cabbage celery sowing greenhouse vegetable seed agricultural machinery	1	1	297	1		0	4.6	13.0	4.6	4.5	1	1	1	1	85.5	105.5						

946	seed cleaning sorting machine for farm agriculture machine	1	1	368	1		0	5.0	9.0	5.0	5.0	1	1	1	1	5100.0	5250.0						

947	automatic irrigation system and sprayer hose agricultural machinery	1	1	122	1		0	0.0	0.0	0.0	0.0	1	1	1	1	11371.0	13371.0						

948	chinese factory price agricultural machinery mf504 tractor in stock	1	1	308	1		0	5.0	10.0	5.0	5.0	1	1	1	1	5000.0	8000.0						

949	china agricultural machines chicken cow dung drying machine	1	1	39	1		0	4.5	2.0	4.5	4.5	1	1	1	1	1718.0	1773.0						

950	tractor for tractor small 4x4 farming machine agricultural	1	1	463	1	CE	0	5.0	1.0	5.0	5.0	1	1	1	1	4526.0	4625.0						

951	high-efficiency farm hay cutter - agricultural machinery feed processing machine	1	1	464	1		0	5.0	15.0	4.9	4.9	1	1	1	1	100.0	120.0						

952	chicken food making machine animal feed pellet feed processing machines agricultural machine	1	1	465	1		0	0.0	0.0	0.0	0.0	1	1	1	1	300.0	1500.0						

953	berserk agricultural machinery equipment mini round hay silage baler machine with crushing function	1	1	278	1		0	5.0	4.0	5.0	5.0	1	1	1	1	14428.57	14428.57						

954	agricultural machinery 1.2 meter cutting width heavy duty flail mower fit on excavator and skid steer loader	1	1	466	1		26	4.9	19.0	4.8	4.6	1	1	1	1	990.0	1410.0						

955	agricultural machinery 20 disc harrow	1	1	467	1		0	0.0	0.0	0.0	0.0	1	1	1	1	463.0	463.0						

956	agriculture machinery v- notched sara (ridger) made in india cultivator parts at best price	1	5	468	1		0	0.0	0.0	0.0	0.0	1	1	1	1	500.0	1500.0						

957	15 hp mini tractor 2 wheel drive 4 wd tractor farm tractor agricultural machine	1	1	469	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1280.0	1500.0						

958	mini tractor agricultural machinery made in china	1	1	470	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5250.0	5300.0						

959	40hp mini tractor agricultural machinery with great price and high durability	1	1	471	1		0	5.0	1.0	5.0	5.0	1	1	1	1	4400.0	4500.0						

960	small farm tractors with rubber tracks crawler tractor agricultural machinery 25 hp mini crawler tractor for sale	1	1	472	1		0	4.2	21.0	4.2	4.3	1	1	1	1	900.0	1089.0						

961	high productivity wheat harvest combain 50hp small agricultural machine lmanual min rice harvesting machine for wet field	1	1	373	1		0	3.0	2.0	4.3	5.0	1	1	1	1	15000.0	16000.0						

962	mini chuff straw crusher agricultural machinery wheat cutting machines for animal silage shredder	1	1	473	1		0	4.9	10.0	4.8	4.5	1	1	1	1	519.0	799.0						

963	tractor implements 3 discs plow mf disc plough agricultural machinery	1	3	133	1		0	5.0	4.0	5.0	5.0	1	1	1	1	250.0	350.0						

964	50hp 80hpnew designed agricultural machinery and equipment remote control mini crawler cultivator mini crawler tractors for sale	1	1	309	1		0	4.5	30.0	4.5	4.5	1	1	1	1	5199.0	5199.0						

965	soil preparation machine bed former for agricultural machine plastic mulch and drip layer machine soil ridger potato ridger	1	1	238	1		0	4.6	49.0	4.7	4.6	1	1	1	1	1300.0	2000.0						

966	2021 promotion season 7hp power weeder small rototiller agricultural machinery and equipment	1	1	474	1		0	0.0	0.0	0.0	0.0	1	1	1	1	342.0	372.0						

967	mini type rice wheat reaper and binder 4g150 farm machine rice agricultural machinery min harvester machine	1	5	280	1		0	0.0	0.0	0.0	0.0	1	1	1	1	949.0	999.0						

968	multipurpose agricultural machinery -10hp two wheel rotary tillage equipment - trencher and winder	1	1	2	1		0	0.0	0.0	0.0	0.0	1	1	1	1	455.0	455.0						

969	combined silage baler and wrapping machine forage silage baler agricultural machinery	1	1	475	1		0	4.9	26.0	4.9	5.0	1	1	1	1	2700.0	3200.0						

970	high standard massey ferguson tractor 290 agricultural machinery 4wd tractor with td order the best tractors online	1	1	386	1		0	0.0	0.0	0.0	0.0	1	1	1	1	900.0	1600.0						

971	agriculture machinery equipment cultivator tiller tractor 24 rotary disc harrow for sale	1	1	476	1		0	0.0	0.0	0.0	0.0	1	1	1	1	420.0	2450.0						

972	factory quality mini keye power tiller agricultural machinery and equipment	1	1	379	1		0	5.0	4.0	5.0	5.0	1	1	1	1	890.0	910.0						

973	most popular rice planting machine rice color sorter machine agricultural machinery	1	1	477	1		0	0.0	0.0	0.0	0.0	1	1	1	1	12928.0	14948.0						

974	air cleaning separating machine paddy cleaner destoner rice separator machine agricultural machinery	1	1	478	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5300.0	6300.0						

975	newest multifunctional mini farm tractor 4wd agriculture machine	1	1	279	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4300.0	6600.0						

976	luke 3tg chinese modern small-scale manual used korea tractor agricultural machinery for sale made in china in bangladesh	1	1	479	1		0	0.0	0.0	0.0	0.0	1	1	1	1	220.0	1200.0						

977	kubota 1008q agriculture machinery combine harvester for rice and wheat	1	1	326	1		0	0.0	0.0	0.0	0.0	1	1	1	1	8000.0	8800.0						

978	drive shaft clutch agricultural machinery	1	50	480	1		0	0.0	0.0	0.0	0.0	1	1	1	1	34.0	34.0						

979	agricultural machinery farming equipment agricole rotovator rototiller manual petrol power motor tiler tiller cultivator	1	1	304	1		0	0.0	0.0	0.0	0.0	1	1	1	1	93.0	93.0						

980	large assortment trommel screen agriculture machinery & equipment organic fertilizer sieving machine	1	1	370	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	8000.0						

981	multi-function remote control lawn mower agriculture machine	1	1	241	1		0	4.6	10.0	4.2	3.7	1	1	1	1	606.0	1000.0						

982	quality new hollands ford 8340 new holland tractor 7840 4 wheel drive agricultural machinery	1	1	481	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	3000.0						

983	farm use chicken animal feed machine mixer and crusher dry wet feed grinder agriculture machinery	1	1	369	1		1	4.6	15.0	4.7	4.7	1	1	1	1	736.0	780.0						

984	hot sale hand push grass cutter machine two stroke agricultural machinery mini gasoline power agricultural rotary tiller	1	1	482	1		0	5.0	10.0	5.0	5.0	1	1	1	1	72.0	75.0						

985	corn thresher household small new hand-cranked grain machine agricultural machinery	1	20	420	1		0	4.5	32.0	4.6	4.6	1	1	1	1	0.99	1.39						

986	competitive price large agricultural machinery wheat and rice harvester thresher machine	1	1	389	1		0	0.0	0.0	0.0	0.0	1	1	1	1	38800.0	39300.0						

987	agricultural machinery comfortable operating environment walk behind two wheel tractor cultivator/scythe mower/plough	1	1	298	1		0	5.0	1.0	5.0	5.0	1	1	1	1	705.0	705.0						

988	52cc hand push gasoline garden cultivators high efficiency two or four stroke agricultural machinery & equipment	1	1	117	1		0	0.0	0.0	0.0	0.0	1	1	1	1	74.0	100.0						

989	agricultural machines carrot onion hand seeding machine	1	1	483	1		0	5.0	1.0	4.6	4.0	1	1	1	1	180.0	200.0						

990	agriculture machine new hot sales tractor 3 ridge plow cultivator farm tools for tractor	1	1	220	1		1	5.0	1.0	5.0	5.0	1	1	1	1	900.0	900.0						

991	medium peanut harvesting groundnut picker agricultural machinery	1	1	385	1		0	5.0	1.0	5.0	5.0	1	1	1	1	600.0	680.0						

992	agricultural machinery heavy duty disc harrow	1	1	484	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2300.0	2300.0						

993	177f/p agriculture machinery 2 wheel drive power rotary tiller cultivators 7hp 9hp power diesel tiller cultivator	1	1	293	1		1	4.8	11.0	4.6	4.6	1	1	1	1	685.0	685.0						

994	agricultural machinery equipment tractor mounted 6 rows garlic planter garlic seeder sowing machine	1	1	231	1		1	4.8	6.0	4.8	4.8	1	1	1	1	760.0	800.0						

995	diesel engine mini rice wheat thresher machine portable agricultural machinery manual millet grain bean seed threshing machines	1	1	200	1		0	4.4	8.0	4.3	4.2	1	1	1	1	220.0	330.0						

996	agriculture machinery farm mini combined crawler world harvesters machine 102 hp for paddy rice small	1	1	375	1		0	0.0	0.0	0.0	0.0	1	1	1	1	14500.0	15200.0						

997	agricultural machinery agro seeds cleaning grape seed separator and dryer rice de-stoning machine	1	1	485	1		0	3.0	2.0	3.0	3.0	1	1	1	1	3050.0	3150.0						

998	stainless steel hot sales portable agricultural machine wheat rice corn paddy grain dryer for sale	1	1	285	1		0	4.6	32.0	4.6	4.6	1	1	1	1	738.0	780.0						

999	high quality china horsen agriculture machinery 210 hp 220 hp 230 hp 4 wd big farm tractor for sale	1	1	486	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4750.0	4990.0						

1000	reasonable price high quality 13-15hp two wheel walking tractor power flail mower small agricultural machine	1	10	374	1		0	5.0	2.0	5.0	5.0	1	1	1	1	500.0	700.0						

1001	best-selling agricultural machinery equipment olive pickers olive shake harvester machine	1	2	487	1		0	0.0	0.0	0.0	0.0	1	1	1	1	151.0	252.0						

1002	agrotk agricultural machinery and equipment rotavator stone buriers soil cultivator for removing stone stock available	1	1	421	1		0	3.2	4.0	2.7	1.7	1	1	1	1	1200.0	1280.0						

1003	traktor farm tractor 50hp 60hp chinese cheap wheel tractor agricultural machine	1	1	488	1		0	4.7	6.0	4.8	4.8	1	1	1	1	3500.0	8000.0						

1004	2024 automatic agricultural machinery high quality grain threshing machine and rice cereal wheat thresher machine	1	1	489	1		5	4.7	21.0	4.8	4.8	1	1	1	1	262.0	478.0						

1005	export quality heavy agricultural machinery in tractors for cultivation and harvesting purposes from india	1	1	490	1		0	0.0	0.0	0.0	0.0	1	1	1	1	10000.0	10000.0						

1006	round baler small agriculture machinery	1	1	382	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	1600.0						

1007	new designed agricultural machinery and equipment mini crawler cultivator mini crawler tractors for sale	1	1	387	1	CE	0	4.4	76.0	4.3	4.3	1	1	1	1	488.0	4280.0						

1008	small agricultural machinery, micro tiller soil machine single cylinder gasoline two stroke	1	10	491	1		0	0.0	0.0	0.0	0.0	1	1	1	1	210.0	220.0						

1009	pto provided gearbox rotary cultivator 28 tiller machine agricultural farm cultivator rotavator cultivator machinery 1.5 years	1	1	325	1		0	5.0	3.0	5.0	5.0	1	1	1	1	469.0	550.0						

1010	high productivity harvester agriculture machinery combine harvester for rice and wheat combine harvester	1	1	313	1		0	0.0	0.0	0.0	0.0	1	1	1	1	9000.0	9500.0						

1011	small four -wheel tractor agricultural four -wheel drive rotor plowing machine delivery trench open draft agricultural machine	1	1	172	1		0	3.6	2.0	4.0	4.5	1	1	1	1	1180.0	1230.0						

1012	sell motor farm cultivator worn cultivators agricultural machines	1	1	492	1		0	3.0	1.0	1.6	1.0	1	1	1	1	5980.0	6178.0						

1013	agricultural machinery & equipment tractors two wheel foton lovol 504 tractor made in china	1	1	127	1		0	1.8	3.0	2.1	2.3	1	1	1	1	9000.0	10000.0						

1014	high productivity agricultural machinery core components bearing vegetable seedling transplanter cabbage garlic planting machine	1	1	493	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2000.0	2000.0						

1015	quality square baler mf 1840 small square baler hot selling agricultural machinery & equipment	1	1	494	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	2500.0						

1016	china farm tractor agricultural machine 180hp 4x4 lt1804	1	1	417	1		0	5.0	11.0	5.0	5.0	1	1	1	1	18000.0	21000.0						

1017	high-precision 2bmq-9a seeder easy-to-use agricultural machinery & equipment other seeders	1	1	495	1		0	0.0	0.0	0.0	0.0	1	1	1	1	46250.0	46250.0						

1018	strict quality check manufacturer agricultural machinery ce forage baler machine	1	1	382	1		0	4.5	1.0	4.5	5.0	1	1	1	1	8500.0	9000.0						

1019	agricultural machinery kubota combine grain harvester for farms / new kubota combine grain harvesting equipment.	1	1	496	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0						

1020	agricultural machinery and equipment for long-term use agricultural machinery hay balers for sale	1	1	154	1		0	0.0	0.0	0.0	0.0	1	1	1	1	20000.0	20000.0						

1021	china eco-friendly agriculture machinery equipment cow dung screw press dewatering machine	1	1	497	1		1	5.0	26.0	5.0	5.0	1	1	1	1	1550.0	1650.0						

1022	new type high productivity 4x4 versatile erreppi buffalo agricultural machinery for quick transport	1	1	498	1		0	0.0	0.0	0.0	0.0	1	1	1	1	10935.0	15000.0						

1023	hot sale wheat corn manual hand push seeder planter agricultural machine for africa	1	50	499	1		1	4.0	5.0	4.3	4.4	1	1	1	1	38.0	50.0						

1024	lg2023 agricultural tractor, 1204 tractor, agricultural machinery	1	1	320	1		0	0.0	0.0	0.0	0.0	1	1	1	1	11242.0	11242.0						

1025	surri mini tractor small agriculture machine for corn harvester efficient crop collector	1	1	500	1		0	4.0	1.0	4.6	5.0	1	1	1	1	300.0	300.0						

1026	rcm straw crusher machine and hay corn crusher machine for making animal feed farm agricultural machinery corn crusher	1	1	502	1		0	5.0	12.0	4.7	4.5	1	1	1	1	550.0	680.0						

1027	china exports agricultural machinery and equipment factory wind cleaning machine grain/spice seed wind impurity removal machine	1	1	422	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5880.0	6280.0						

1028	high quality zero till seed fertilizer drill seeding & plantation agricultural machinery available at reasonable price	1	1	123	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1185.0	1520.0						

1029	high efficient agriculture machinery equipment/extractor juicer/waste vegetable shredder and compost machine	1	1	503	1		1	5.0	7.0	5.0	5.0	1	1	1	1	3750.0	3800.0						

1030	agricultural machinery and equipment agricultural fertilizer irrigation machine multi-functional hydroponic machine	1	1	504	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2680.0	3000.0						

1031	new quality agriculture machinery combine harvester for rice and wheat cheap combine harvester available	1	1	318	1		0	4.5	2.0	4.3	4.0	1	1	1	1	24000.0	24000.0						

1032	manual type garden cultivator tiller machine hand tiller agricultural machinery & equipment	1	1	105	1		1	4.6	29.0	4.2	4.1	1	1	1	1	25.0	58.0						

1033	multi functional new diesel mini hand cralwer walking tractor agriculture machinery mini tiller machine	1	1	505	1		0	5.0	4.0	4.9	5.0	1	1	1	1	399.0	482.0						

1034	china 20hp 30hp 40hp 50hp mini tractors prices list farm tractors agricultural machinery and agricultural equipment tractors	1	1	13	1		0	0.0	0.0	0.0	0.0	1	1	1	1	6500.0	6500.0						

1035	wide use agricultural machinery & equipment 2000 chicken incubator and hatching machine	1	1	506	1		0	4.8	14.0	4.7	4.7	1	1	1	1	350.0	380.0						

1036	massey ferguson 399 agricultural machinery / used 85hp farm tractor available for sale	1	1	169	1		0	0.0	0.0	0.0	0.0	1	1	1	1	2500.0	2500.0						

1037	agricultural machinery and equipment remote control mini crawler cultivator mini crawler tractors for sale	1	1	507	1		0	5.0	5.0	5.0	5.0	1	1	1	1	998.0	3550.0						

1038	china large capacity eco-friendly agriculture machine type and new condition dewatering screw press	1	1	508	1	CE	0	4.6	3.0	4.8	5.0	1	1	1	1	3200.0	3200.0						

1039	zoomlion agriculture machine 4lzt-5.0qc rice combine harvester with cheap price for sale	1	2	509	1		0	4.7	3.0	4.6	4.6	1	1	1	1	63000.0	63000.0						

1040	agricultural machinery and equipment - hand tractor 8/10/12hp	1	1	371	1		0	1.0	1.0	2.3	3.0	1	1	1	1	900.0	900.0						

1041	selling durable and efficient cattle farm farming agricultural machinery and equipment feed mixer tmr	1	1	510	1		0	5.0	1.0	5.0	5.0	1	1	1	1	8200.0	8219.0						

1042	used/second hand farm wheel tractors massey ferguson mf1004 100hp 4x4wd with small mini compact agricultural equipment machinery	1	2	235	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1499.0	1499.0						

1043	tracked tractor crawler farm use,mini agricultural crawler tractors 120hp type news agricultural machinery & equipment 2wd	1	1	240	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3718.0	4613.0						

1044	agriculture machinery combine harvester for corn( maize) and wheat	1	1	130	1		0	5.0	1.0	5.0	5.0	1	1	1	1	81000.0	82000.0						

1045	high productivity mist blower sprayer back pack sprayer boom sprayer agricultural machinery	1	500	511	1	EMC,CE	500	5.0	7.0	5.0	5.0	1	1	1	1	33.2	36.0						

1046	china factory hot-selling 65hp double-row corn harvester large agricultural machinery maize harvesting machine	1	1	372	1		0	4.7	12.0	4.7	4.8	1	1	1	1	9600.0	10000.0						

1047	agricultural machinery 2023 case ih8250 combine harvester sugarcane, soybean ,wheat, rice combine harvester for sale	1	2	512	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1200.0	1200.0						

1048	2204 cheap price for agricultural machinery 50-220 hp wheel tractor	1	1	295	1		0	4.0	1.0	4.3	4.0	1	1	1	1	42000.0	43000.0						

1049	lisa high efficiency hot sale furrow plow with 2 blades -agricultural machinery	1	1	161	1		0	4.0	3.0	3.7	3.6	1	1	1	1	129.0	159.0						

1050	front mounted agricultural machinery matched with popular tractors	1	1	513	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	3000.0						

1051	top quality china new make good price 904 model 90hp farm tractor agricultural machine with radial tyre for sale	1	1	514	1		0	5.0	3.0	5.0	5.0	1	1	1	1	6260.0	6650.0						

1052	de arado 3 discos reversible/disc plough price/agricultural machinery	1	1	515	1		0	4.8	4.0	4.9	5.0	1	1	1	1	1220.0	1350.0						

1053	commercial small rice portable agricultural rice milling machine fresh rice machine peeling machine	1	5	303	1		0	4.3	53.0	4.3	4.3	1	1	1	1	199.0	210.0						

1054	best wholesale farm boom sprayer 500l 1000l pump marketing equipment agricultural machinery now available for sale	1	2	516	1		0	0.0	0.0	0.0	0.0	1	1	1	1	270.0	380.0						

1055	agriculture machinery & equipment mini furrow plough for tractor made in north india 3 blade disc plow	1	5	271	1		0	0.0	0.0	0.0	0.0	1	1	1	1	600.0	600.0						

1056	farm tractors agricol 4x4 40hp mfarming machine for sale agricultural machinery tractor front loader price	1	1	239	1		0	5.0	3.0	5.0	5.0	1	1	1	1	3100.0	3200.0						

1057	rx220h farming equipment agricultural machine rotary tiller rotavator cultivator	1	2	517	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1300.0	1500.0						

1058	agriculture machine hand held weeding machine / mini gasoline power weeder	1	200	518	1		0	5.0	3.0	5.0	5.0	1	1	1	1	65.0	80.0						

1059	hot-selling 1ls-7 subsoiler agricultural machinery for sale	1	1	333	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1500.0	1500.0						

1060	hot sale product gs1028 high quality harvester maize combine harvester agriculture machinery for southeast asian market	1	1	519	1		0	0.0	0.0	0.0	0.0	1	1	1	1	13000.0	13000.0						

1061	agricultural equipment farm agricultural machinery & equipment 70hp 704 tractor tractors for agriculture	1	1	520	1		0	5.0	2.0	5.0	5.0	1	1	1	1	6200.0	6300.0						

1062	high quality farm machine agricultural machinery & equipment maize sheller for sale in south africa	1	1	378	1		0	4.7	11.0	4.5	4.2	1	1	1	1	85.8	99.8						

1063	mini tiller 52cc cultivator agricultural machine hand tiller agricultural machinery & equipment	1	1	377	1		0	4.9	6.0	4.8	4.8	1	1	1	1	78.0	158.0						

1064	cheap kubota m954k farm tractor agricultural machinery and equipment	1	1	521	1		0	0.0	0.0	0.0	0.0	1	1	1	1	5242.79	12435.59						

1065	agricultural machinery of kubota similar wheat rice combine harvester	1	1	522	1		0	5.0	1.0	5.0	5.0	1	1	1	1	12330.0	12880.0						

1066	farm agricultural machinery wet and dry double roll jet rice polisher rice mill milling machine with cyclone	1	1	322	1		0	4.0	17.0	4.1	4.1	1	1	1	1	950.0	950.0						

1067	salable labor-saving intertillage agriculture machines for farm	1	1	376	1		0	5.0	1.0	5.0	5.0	1	1	1	1	501.0	529.0						

1068	customized agriculture machinery farm laminating machine farm ridging machine	1	1	328	1		0	0.0	0.0	0.0	0.0	1	1	1	1	500.0	500.0						

1069	cassava harvesting machine cassava harvester tractor implements agricultural machinery	1	1	523	1		0	5.0	6.0	5.0	5.0	1	1	1	1	7500.0	8500.0						

1070	agriculture machinery micro 15hp gas motor walk behind trencher machine	1	1	524	1		0	0.0	0.0	0.0	0.0	1	1	1	1	690.0	840.0						

1071	factory supply granulator pellet animal feed machine fodder pellet mill for agricultural machinery and equipment	1	1	525	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4800.0	4800.0						

1072	fairly used agriculture machinery combine harvester new-holland cr9060 for rice and wheat cheap combine harvester from austria	1	1	526	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1000.0	1500.0						

1073	deutz fahr tractor agricultural machinery & equipment	1	1	415	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3000.0	3000.0						

1074	agriculture machinery multipurpose diesel engine 35hp rice paddy tiller crawler tractor land tiller machinery	1	1	527	1		0	0.0	0.0	0.0	0.0	1	1	1	1	1690.0	1800.0						

1075	hot sale agricultural machines animal food maker feed granulator machine pellet mill machine for fish chicken duck rabbit	1	1	529	1		0	0.0	0.0	0.0	0.0	1	1	1	1	537.0	539.0						

1076	china agricultural equipment mini farm tractor machine wheel tractor agricultural machine price	1	1	530	1		0	5.0	3.0	5.0	5.0	1	1	1	1	2000.0	4200.0						

1077	cheap professional agricultural machine sugarcane cultivator fertilization hiller high efficiency cultivator machine	1	1	153	1		0	0.0	0.0	0.0	0.0	1	1	1	1	3350.0	3700.0						

1078	agricultural equipment farm agricultural machinery	1	1	531	1		2	5.0	3.0	5.0	5.0	1	1	1	1	4500.0	4900.0						

1079	hand held garden tiller gasoline cultivator 212cc diesel engine agriculture machine	1	1	532	1		10	4.7	13.0	4.6	4.5	1	1	1	1	219.0	259.0						

1080	grass chopper picadora de pasto con motor chaff cutter animal feed processing machine agricultural machinery	1	1	533	1		0	0.0	0.0	0.0	0.0	1	1	1	1	699.0	699.0						

1081	lovol 1204 4wd wheel tractor new agricultural machinery with core motor components for home use	1	1	230	1		0	0.0	0.0	0.0	0.0	1	1	1	1	16000.0	16000.0						

1082	agriculture machinery 1850 working width tractor pto rotary tiller 1gqn-200	1	1	310	1		1	4.4	21.0	4.2	4.1	1	1	1	1	700.0	750.0						

1083	tractors agricultural machinery and cultivated land multi-purpose tractors machine agriculture wheel tractor	1	1	79	1	CE	0	5.0	1.0	5.0	5.0	1	1	1	1	9500.0	10200.0						

1084	factory direct sales of agricultural machinery and equipment small tractors	1	1	535	1		0	0.0	0.0	0.0	0.0	1	1	1	1	4000.0	4000.0						

1085	sprayers agricultural machinery the spraying machine is used for agricultural orchard management	1	1	536	1		0	0.0	0.0	0.0	0.0	1	1	1	1	386.3	415.3						

1086	compact farm tractor agricultural machine 25hp 30hp 35hp 130hp 150hp 180hp lt1804	1	1	412	1		0	0.0	0.0	0.0	0.0	1	1	1	1	17000.0	19000.0						



### Installation
First things first you must to have Python3.11 or higher installed 

It's recommended to use [pipx](https://pypa.github.io/pipx/) instead of pip for end-user applications written in Python. `pipx` installs the package, exposes his CLI entrypoints in an isolated environment and makes it available everywhere this guarantees no dependency conflicts and clean uninstall. If you'd like to use `pip` instead, just replace `pipx` with `pip`  but obviously  as usual you'll need to  create a virtual environment and activate it before to use `aba-cli-scrapper` to avoid any dependency conflicts issues. let's install `aba-cli-scrapper` using pipx:

   ```shell
      pipx install aba-cli-scrapper
   ```

  
## Using the CLI Interface
 

**Need Help?**  run  any commands followed by `--help` for detailed informations about its usage and options. For example: `aba-run --help` will show you all subcommands available and how to use them.

<div align="center">
  <p>
    <a href="#"><img src="images\help-cli.png" width="900" height="340" alt="command result 1" /></a>
  </p>
  <p align="center">
  </p>
</div>

#### Available Commands:

**Warnings:** 
- `aba-run` is the base command means all other commands that will be introduce bellow are sub-commands and should always be preceded by  `aba-run`.
Practice make perfect isn't ? So let's get started with a use case example. 
Let's assume  that you want to scrape data about `electric bikes` from Alibaba.com.


---
<details>
<summary>Scraper Demo</summary>

[https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4](https://private-user-images.githubusercontent.com/52409392/351958081-302e7586-7e73-495f-bb40-41b8002c0480.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4ODE5NTUsIm5iZiI6MTcyMTg4MTY1NSwicGF0aCI6Ii81MjQwOTM5Mi8zNTE5NTgwODEtMzAyZTc1ODYtN2U3My00OTVmLWJiNDAtNDFiODAwMmMwNDgwLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDA0MjczNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQwZjlhM2I5ODk5ZjYzYmRhNmI5OWJhMzMxMDU2MGQ4NTBiZTk0OTAzNDg5M2M3NTU1M2NhYzFkYTc1YzQ5YzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.xOTTGRRU8UQ8YZFMegl_TJC6kvtCR4aQEwJyp_DAjjk)

</details>


*   **`scraper` sub-command:**  Initiates scraping of Alibaba.com based on the provided keywords.
this command takes two required arguments and one optional argument:
    * -  **`key_words` (required):** The search term(s) for finding products on Alibaba. Enclose multiple keywords in quotes.
    * - **`--page-results` or `-pr` (required):** Usually keys words will results to many pages macthing them. Then you must to indicate how many of them you want to pull out.If any value is not provided `10` will be used by default.
    * -  **`--html-folder` or `-hf` (optional):** Specifies the directory to store the raw HTML files. If omitted, a folder with sanitized keywords as name will be automatically created. In this case `electric_bikes` will be used as a results folder name.

    **Example**:
    ```shell
    aba-run scraper "electric bikes" -hf "bike_results" -pr 15
    ```
by default `scrapper` will use async mode which supported by brightdata api which means if you want to use it you will need to provide your api key. set it by using :
   ```bash
   aba-run set-api-key your_api_key
   ```
   and now run `scraper` sub-command without `--sync-api` flag to use async mode.
   However if you want to use sync mode you can use :
   ```bash
   aba-run scraper "electric bikes" -hf "bike_results" -pr 15  --sync-api
   ```
    and voila! 

Now `bike_results` (since you already provided name you wish to have) directory has been created and should contains all html files from alibaba.com matching your keywords.

---

<details>
<summary>db-init Demo with sqlite</summary>

[https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4](https://private-user-images.githubusercontent.com/52409392/351970999-0f9491e5-69f0-470b-8a8e-9e436f0a0d0b.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4ODQ0MjksIm5iZiI6MTcyMTg4NDEyOSwicGF0aCI6Ii81MjQwOTM5Mi8zNTE5NzA5OTktMGY5NDkxZTUtNjlmMC00NzBiLThhOGUtOWU0MzZmMGEwZDBiLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDA1MDg0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRiMmJiZTg3MDE3NTAwZWRhMzE2MTM5NDhjNmZkZTAwZWYxOTUxN2RlMzA1NGM4MzgyNWJkZTJmNTNkNzFhNDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.gjlDs3VMK_MIg1Ne3cEqrO__LsZdyOgjy-SlZuXvd_s)

</details>
Then you must initialize a database. Mysql and sqlite are supported.

*   **`db-init` sub-command:** Creates a new database mysql/sqlite.
this command takes one required arguments and six optional arguments(depends on engine you choose):
    * -   **`engine` (required):** Choose either `sqlite` or `mysql`.
    *  - **`--sqlite-file` or `-f`(optional, SQLite only):**  The name for your SQLite database file (without any extension).
    *   - **`--host` or `-h`, `--port` or `-p`, `--user` or `-u`, `--password` or `-pw`, `--db-name`or `-db` (required for MySQL):**  Your MySQL database connection details.
  
    *   **`--only-with` or `-ow`(optional Mysql):**  If you just want to update some details of your credentials in `db_credentials.json` file but not all before to initialize a brand new database.
* **NB:** `--host` and `--port` are respectively set to `localhost` and `3306` by default. 

**MySQL Use case:**
  ```shell
  aba-run db-init mysql -u "mysql_username" -pw "mysql_password" -db "alibaba_products" 
  ```
Assuming that you have already initialized your database,and you want to created a new one with a new database name without to set password and username again , simply run :

  ```shell
  aba-run db-init mysql --only-with -db "alibaba_products" 
  ```

**NB: When you initialize your mysql as engine, the `db-init` sub-command will save your credentials in `db_credentials.json` file, so when you will need to update your database, simply run `aba-run db-update  mysql --kw-results bike_results\` to automatically update your database by using your saved credentials**


**SQLite Use case :**
  ```shell
  aba-run db-init sqlite --sqlite-file alibaba_data
  ```
db-init subcommand will try to use sqlite engine by default  so if you are planning to use it run as bellow :

**SQLite Use case V2 :**
  ```shell
  aba-run db-init -f alibaba_data
  ```

As soons as your database has been initialized, you can update it with the scraped data.

---

<details>
<summary>db-update Demo</summary>

[https://user-images.githubusercontent.com/49741340/238535232-459847af-a15c-4d9b-91ac-fab9958bc74f.mp4](https://private-user-images.githubusercontent.com/52409392/351977812-ecfe8e3b-af20-4611-a07d-dd6ac401bf8c.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4ODY1NjgsIm5iZiI6MTcyMTg4NjI2OCwicGF0aCI6Ii81MjQwOTM5Mi8zNTE5Nzc4MTItZWNmZThlM2ItYWYyMC00NjExLWEwN2QtZGQ2YWM0MDFiZjhjLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDA1NDQyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY4OTI3NDY0OThmYTA5NDJiMTEyMjBhZjczNDE2M2RkZWNlMmRjMzUyZjBkODgwMjY2NTc1NzQ1NjI5MTBmMzcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Fa2jqUTAg-MQ-J33x6x_UIjnId190KhdEJZbUmmbTiw)

</details>

*  **`db-update` sub-command:** add scraped data from html files to your database (you can't use this command twice with same database credentals to avoid UNIQUE CONSTRAINT ERROR).

this command takes two required arguments and two optional arguments:
   * - **`--db-engine` (required):** Select your database engine: `sqlite` or `mysql`.
   * -  **`--kw-results` (required):**  The path to the folder containing the HTML files generated by the `scraper` sub command.
   * - **`--filename` (required for SQLite):** If you're using SQLite, provide the desired filename for your database. whitout any extension.
   * - **`--db-name` (optional for MySQL):** If you're using MySQL,and want to push the data to a different database, provide the desired database name.

  **MySQL Use case:**
  ```bash
  aba-run db-update  mysql --kw-results bike_results\ 
  ```
**NB:What if you want to change something while you updating the database? Assuming that you have run another scraping command and you want to save this data in another database name whitout update credential file or rewriting all theses parameter just to change your database name then, simply run `aba-run db-update  mysql --kw-results another_keyword_folder_result\ --db-name "another_database_name"`.**

  **SQLite Use case:**
   ```shell
   aba-run db-update  sqlite --kw-results bike_results\ --filename alibaba_data
   ```
---
*  **`export-as-csv` sub-command:** Exports scraped data from your sqlitedatabase to a CSV file. This csv file will contain a `FULL OUTER JOIN` with the `products` and `suppliers` tables.

this command takes one required argument and one optional argument:
   * -  **`--sqlite_file` (required):** The name for your SQLite database file with his extension.
   * -  **`--to` or `-t` (required):**  The name for your CSV file with his extension.



## Future Enhancements

This project has a lot of potential for growth! Here are some exciting features I'm considering for the future:


-  **Retrieval Augmented Generation (RAG):** Integrate a RAG system that allows users to ask natural language questions about the scraped data, making it even more powerful for insights.

## Contributions Welcome!

I believe in the power of open source! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. I'm always open to new ideas and improvements.

## License

This project is licensed under the [Gnu General Public License Version **3**](COPYING).


  
