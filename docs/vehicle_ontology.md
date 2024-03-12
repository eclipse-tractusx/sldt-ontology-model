



# Vehicle Ontology


**Title:**  Vehicle Ontology

**Description:**  Ontology for vehicles in the automotive industry.

**Creator:**  Zazralt Magic

**Contributor:**  Rolf Bosse, Jörg Schulz, Oguzhan Balandi

**Date:**  2023-02-21

**Version:**  1.9.4  
  
![ontology](images/vehicle_ontology.gv.svg)  

## Classes
  

|Name|Description|Datatype properties|Object properties|Subclass of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="EClassType">EClassType</span>|None|[classification](#classification) , [irdi](#irdi) ||[https://w3id.org/catenax/ontology/core#ConceptualObject](#https://w3id.org/catenax/ontology/core#ConceptualObject) |
|<span id="Part">Part</span>|None|[batteryInformation](#batteryInformation) , [bodyInformation](#bodyInformation) , [chassisInformation](#chassisInformation) , [engineInformation](#engineInformation) , [partInformation](#partInformation) , [powertrainInformation](#powertrainInformation) , [suspensionInformation](#suspensionInformation) |[hasSubpart](#hasSubpart) , [isPartOf](#isPartOf) , [isSubpartOf](#isSubpartOf) , [supplier](#supplier) |[https://w3id.org/catenax/ontology/core#PhysicalObject](#https://w3id.org/catenax/ontology/core#PhysicalObject) |
|<span id="Vehicle">Vehicle</span>|None|[acceleration](#acceleration) , [adblueTankCapacity](#adblueTankCapacity) , [age](#age) , [airConditioningType](#airConditioningType) , [assistanceSystem](#assistanceSystem) , [batteryCapacity](#batteryCapacity) , [batteryInformation](#batteryInformation) , [batteryWeight](#batteryWeight) , [bodyInformation](#bodyInformation) , [bodyStyle](#bodyStyle) , [bore](#bore) , [brand](#brand) , [breaking](#breaking) , [camshaftValvetrainConfiguration](#camshaftValvetrainConfiguration) , [cargoInformation](#cargoInformation) , [cargoVolume](#cargoVolume) , [chargingTime](#chargingTime) , [chassisInformation](#chassisInformation) , [clutchType](#clutchType) , [co2Emissions](#co2Emissions) , [co2EmissionsWltp](#co2EmissionsWltp) , [communicationInformation](#communicationInformation) , [configuration](#configuration) , [curbWeight](#curbWeight) , [developmentSeries](#developmentSeries) , [dragCoefficient](#dragCoefficient) , [driveWheelType](#driveWheelType) , [dryWeight](#dryWeight) , [electricConsumption](#electricConsumption) , [electricPower](#electricPower) , [electricRange](#electricRange) , [electricRangeWltp](#electricRangeWltp) , [emissionClass](#emissionClass) , [engineAlignment](#engineAlignment) , [engineAspiration](#engineAspiration) , [engineCompressionRatio](#engineCompressionRatio) , [engineDisplacement](#engineDisplacement) , [engineFamily](#engineFamily) , [engineForm](#engineForm) , [engineFuelInjection](#engineFuelInjection) , [engineGeneration](#engineGeneration) , [engineInformation](#engineInformation) , [engineManufacturer](#engineManufacturer) , [engineMaxPower](#engineMaxPower) , [engineMaxTorque](#engineMaxTorque) , [engineName](#engineName) , [enginePerformanceClass](#enginePerformanceClass) , [enginePosition](#enginePosition) , [engineSeries](#engineSeries) , [engineTypeCode](#engineTypeCode) , [engineVersion](#engineVersion) , [euEnergyLabel](#euEnergyLabel) , [euroCarSegment](#euroCarSegment) , [expectedLifetime](#expectedLifetime) , [expectedLifetimeMileage](#expectedLifetimeMileage) , [exteriorColor](#exteriorColor) , [frontBrakeDiscDiameter](#frontBrakeDiscDiameter) , [frontSpringType](#frontSpringType) , [frontSuspension](#frontSuspension) , [fuelConsumptionCity](#fuelConsumptionCity) , [fuelConsumptionCombined](#fuelConsumptionCombined) , [fuelConsumptionHighway](#fuelConsumptionHighway) , [fuelEfficiency](#fuelEfficiency) , [fuelInformation](#fuelInformation) , [fuelTankCapacity](#fuelTankCapacity) , [fuelType](#fuelType) , [grossVehicleMass](#grossVehicleMass) , [groundClearance](#groundClearance) , [hasAutomaticHeadLights](#hasAutomaticHeadLights) , [hasFogLights](#hasFogLights) , [hasModem](#hasModem) , [hasNavigation](#hasNavigation) , [hasRadio](#hasRadio) , [height](#height) , [infotainmentInformation](#infotainmentInformation) , [interiorColor](#interiorColor) , [interiorInformation](#interiorInformation) , [interiorType](#interiorType) , [length](#length) , [lifetimeInformation](#lifetimeInformation) , [lightingInformation](#lightingInformation) , [location](#location) , [manufacturerKeyNumber](#manufacturerKeyNumber) , [maxAxleLoad](#maxAxleLoad) , [maxPayload](#maxPayload) , [maxSpeed](#maxSpeed) , [maxTowingCapacity](#maxTowingCapacity) , [mileage](#mileage) , [model](#model) , [modelArchitecture](#modelArchitecture) , [modelEndOfProduction](#modelEndOfProduction) , [modelGeneration](#modelGeneration) , [modelInformation](#modelInformation) , [modelSeries](#modelSeries) , [modelStartOfProduction](#modelStartOfProduction) , [modelVariant](#modelVariant) , [numberOfAirbags](#numberOfAirbags) , [numberOfAxles](#numberOfAxles) , [numberOfCylinders](#numberOfCylinders) , [numberOfDoors](#numberOfDoors) , [numberOfDriveAxles](#numberOfDriveAxles) , [numberOfForwardGears](#numberOfForwardGears) , [numberOfPassengers](#numberOfPassengers) , [numberOfSeatRows](#numberOfSeatRows) , [numberOfSeats](#numberOfSeats) , [numberOfStandingPlaces](#numberOfStandingPlaces) , [numberOfValves](#numberOfValves) , [operatingHours](#operatingHours) , [passengerVolume](#passengerVolume) , [performanceInformation](#performanceInformation) , [powertrainInformation](#powertrainInformation) , [powertrainLayout](#powertrainLayout) , [previousVehicleModel](#previousVehicleModel) , [range](#range) , [rangeWltp](#rangeWltp) , [rearSpringType](#rearSpringType) , [rearSuspension](#rearSuspension) , [registrationAuthority](#registrationAuthority) , [registrationDate](#registrationDate) , [registrationInformation](#registrationInformation) , [registrationLocation](#registrationLocation) , [registrationOwner](#registrationOwner) , [registrationPlate](#registrationPlate) , [rim](#rim) , [roadNoise](#roadNoise) , [safetyInformation](#safetyInformation) , [specialUsage](#specialUsage) , [stateDateTime](#stateDateTime) , [stateInformation](#stateInformation) , [stationaryNoise](#stationaryNoise) , [steeringType](#steeringType) , [steeringWheelPosition](#steeringWheelPosition) , [stroke](#stroke) , [suspensionInformation](#suspensionInformation) , [tire](#tire) , [tongueWeight](#tongueWeight) , [trailerWeight](#trailerWeight) , [transmission](#transmission) , [trunkVolume](#trunkVolume) , [turningRadius](#turningRadius) , [typeCode](#typeCode) , [typeCodeNumber](#typeCodeNumber) , [vehicleIdentificationNumber](#vehicleIdentificationNumber) , [warrantyInformation](#warrantyInformation) , [warrantyMaxDuration](#warrantyMaxDuration) , [warrantyMaxMileage](#warrantyMaxMileage) , [weight](#weight) , [weightTotal](#weightTotal) , [wheelbase](#wheelbase) , [width](#width) , [worldManufacturerCountry](#worldManufacturerCountry) , [worldManufacturerId](#worldManufacturerId) , [worldManufacturerName](#worldManufacturerName) , [worldManufacturerRegion](#worldManufacturerRegion) |[hasPart](#hasPart) , [isVariantOf](#isVariantOf) , [manufacturer](#manufacturer) |[https://w3id.org/catenax/ontology/core#PhysicalObject](#https://w3id.org/catenax/ontology/core#PhysicalObject) |
|<span id="VehicleModel">VehicleModel</span>|None|||[https://w3id.org/catenax/ontology/core#ConceptualObject](#https://w3id.org/catenax/ontology/core#ConceptualObject) |

## Data Properties
  

|Name|Description|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="acceleration">acceleration</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="adblueTankCapacity">adblueTankCapacity</span>|None|[Vehicle](#Vehicle) |xml : double |[fuelInformation](#fuelInformation) |
|<span id="age">age</span>|None|[Vehicle](#Vehicle) |xml : integer |[stateInformation](#stateInformation) |
|<span id="airConditioningType">airConditioningType</span>|None|[Vehicle](#Vehicle) |xml : string |[interiorInformation](#interiorInformation) |
|<span id="assemblyCountry">assemblyCountry</span>|None||xml : string |[productionInformation](#productionInformation) |
|<span id="assemblyPlant">assemblyPlant</span>|None||xml : string |[productionInformation](#productionInformation) |
|<span id="assistanceSystem">assistanceSystem</span>|None|[Vehicle](#Vehicle) |xml : string |[suspensionInformation](#suspensionInformation) |
|<span id="batteryCapacity">batteryCapacity</span>|None|[Vehicle](#Vehicle) |xml : integer |[batteryInformation](#batteryInformation) |
|<span id="batteryInformation">batteryInformation</span>|None|[Part](#Part) , [Vehicle](#Vehicle) |||
|<span id="batteryType">batteryType</span>|None||xml : string |[batteryInformation](#batteryInformation) |
|<span id="batteryWeight">batteryWeight</span>|None|[Vehicle](#Vehicle) |xml : integer |[batteryInformation](#batteryInformation) |
|<span id="bodyInformation">bodyInformation</span>|None|[Part](#Part) , [Vehicle](#Vehicle) |||
|<span id="bodyStyle">bodyStyle</span>|None|[Vehicle](#Vehicle) |xml : string |[bodyInformation](#bodyInformation) |
|<span id="bore">bore</span>|None|[Vehicle](#Vehicle) |xml : double |[engineInformation](#engineInformation) |
|<span id="brand">brand</span>|None|[Vehicle](#Vehicle) |xml : string |[modelInformation](#modelInformation) |
|<span id="breaking">breaking</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="camshaftValvetrainConfiguration">camshaftValvetrainConfiguration</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="cargoInformation">cargoInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="cargoVolume">cargoVolume</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="chargingTime">chargingTime</span>|None|[Vehicle](#Vehicle) |xml : double |[batteryInformation](#batteryInformation) |
|<span id="chassisInformation">chassisInformation</span>|None|[Part](#Part) , [Vehicle](#Vehicle) |||
|<span id="classification">classification</span>|None|[EClassType](#EClassType) |xml : string ||
|<span id="clutchType">clutchType</span>|None|[Vehicle](#Vehicle) |xml : string |[powertrainInformation](#powertrainInformation) |
|<span id="co2Emissions">co2Emissions</span>|None|[Vehicle](#Vehicle) |xml : integer |[fuelInformation](#fuelInformation) |
|<span id="co2EmissionsWltp">co2EmissionsWltp</span>|None|[Vehicle](#Vehicle) |xml : integer |[fuelInformation](#fuelInformation) |
|<span id="communicationInformation">communicationInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="configuration">configuration</span>|None|[Vehicle](#Vehicle) |xml : string ||
|<span id="countryOption">countryOption</span>|None||xml : string |[productionInformation](#productionInformation) |
|<span id="curbWeight">curbWeight</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="deliveryCountry">deliveryCountry</span>|None||xml : string |[productionInformation](#productionInformation) |
|<span id="deliveryDate">deliveryDate</span>|None||xml : date |[productionInformation](#productionInformation) |
|<span id="deliveryPrice">deliveryPrice</span>|None||xml : integer |[productionInformation](#productionInformation) |
|<span id="description">description</span>|None||xml : string ||
|<span id="developmentSeries">developmentSeries</span>|None|[Vehicle](#Vehicle) |xml : string |[modelInformation](#modelInformation) |
|<span id="dragCoefficient">dragCoefficient</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="driveWheelType">driveWheelType</span>|None|[Vehicle](#Vehicle) |xml : string |[powertrainInformation](#powertrainInformation) |
|<span id="dryWeight">dryWeight</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="electricConsumption">electricConsumption</span>|None|[Vehicle](#Vehicle) |xml : double |[batteryInformation](#batteryInformation) |
|<span id="electricPower">electricPower</span>|None|[Vehicle](#Vehicle) |xml : integer |[batteryInformation](#batteryInformation) |
|<span id="electricRange">electricRange</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="electricRangeWltp">electricRangeWltp</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="emissionClass">emissionClass</span>|None|[Vehicle](#Vehicle) |xml : string |[fuelInformation](#fuelInformation) |
|<span id="engineAlignment">engineAlignment</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineAspiration">engineAspiration</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineCompressionRatio">engineCompressionRatio</span>|None|[Vehicle](#Vehicle) |xml : double |[engineInformation](#engineInformation) |
|<span id="engineDisplacement">engineDisplacement</span>|None|[Vehicle](#Vehicle) |xml : double |[engineInformation](#engineInformation) |
|<span id="engineFamily">engineFamily</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineForm">engineForm</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineFuelInjection">engineFuelInjection</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineGeneration">engineGeneration</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineInformation">engineInformation</span>|None|[Part](#Part) , [Vehicle](#Vehicle) |||
|<span id="engineManufacturer">engineManufacturer</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineMaxPower">engineMaxPower</span>|None|[Vehicle](#Vehicle) |xml : double |[engineInformation](#engineInformation) |
|<span id="engineMaxTorque">engineMaxTorque</span>|None|[Vehicle](#Vehicle) |xml : double |[engineInformation](#engineInformation) |
|<span id="engineName">engineName</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="enginePerformanceClass">enginePerformanceClass</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="enginePosition">enginePosition</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineSeries">engineSeries</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineTypeCode">engineTypeCode</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="engineVersion">engineVersion</span>|None|[Vehicle](#Vehicle) |xml : string |[engineInformation](#engineInformation) |
|<span id="euEnergyLabel">euEnergyLabel</span>|None|[Vehicle](#Vehicle) |xml : string |[fuelInformation](#fuelInformation) |
|<span id="euroCarSegment">euroCarSegment</span>|None|[Vehicle](#Vehicle) |xml : string |[bodyInformation](#bodyInformation) |
|<span id="expectedLifetime">expectedLifetime</span>|None|[Vehicle](#Vehicle) |xml : integer |[lifetimeInformation](#lifetimeInformation) |
|<span id="expectedLifetimeMileage">expectedLifetimeMileage</span>|None|[Vehicle](#Vehicle) |xml : integer |[lifetimeInformation](#lifetimeInformation) |
|<span id="exteriorColor">exteriorColor</span>|None|[Vehicle](#Vehicle) |xml : string |[bodyInformation](#bodyInformation) |
|<span id="frontBrakeDiscDiameter">frontBrakeDiscDiameter</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="frontSpringType">frontSpringType</span>|None|[Vehicle](#Vehicle) |xml : string |[suspensionInformation](#suspensionInformation) |
|<span id="frontSuspension">frontSuspension</span>|None|[Vehicle](#Vehicle) |xml : string |[suspensionInformation](#suspensionInformation) |
|<span id="fuelConsumptionCity">fuelConsumptionCity</span>|None|[Vehicle](#Vehicle) |xml : double |[fuelInformation](#fuelInformation) |
|<span id="fuelConsumptionCombined">fuelConsumptionCombined</span>|None|[Vehicle](#Vehicle) |xml : double |[fuelInformation](#fuelInformation) |
|<span id="fuelConsumptionHighway">fuelConsumptionHighway</span>|None|[Vehicle](#Vehicle) |xml : double |[fuelInformation](#fuelInformation) |
|<span id="fuelEfficiency">fuelEfficiency</span>|None|[Vehicle](#Vehicle) |xml : double |[fuelInformation](#fuelInformation) |
|<span id="fuelInformation">fuelInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="fuelTankCapacity">fuelTankCapacity</span>|None|[Vehicle](#Vehicle) |xml : double |[fuelInformation](#fuelInformation) |
|<span id="fuelType">fuelType</span>|None|[Vehicle](#Vehicle) |xml : string |[fuelInformation](#fuelInformation) |
|<span id="grossVehicleMass">grossVehicleMass</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="groundClearance">groundClearance</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="hasAutomaticHeadLights">hasAutomaticHeadLights</span>|None|[Vehicle](#Vehicle) |xml : boolean |[lightingInformation](#lightingInformation) |
|<span id="hasFogLights">hasFogLights</span>|None|[Vehicle](#Vehicle) |xml : boolean |[lightingInformation](#lightingInformation) |
|<span id="hasModem">hasModem</span>|None|[Vehicle](#Vehicle) |xml : boolean |[communicationInformation](#communicationInformation) |
|<span id="hasNavigation">hasNavigation</span>|None|[Vehicle](#Vehicle) |xml : boolean |[infotainmentInformation](#infotainmentInformation) |
|<span id="hasRadio">hasRadio</span>|None|[Vehicle](#Vehicle) |xml : boolean |[infotainmentInformation](#infotainmentInformation) |
|<span id="height">height</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="id">id</span>|None||xml : string |[partInformation](#partInformation) |
|<span id="infotainmentInformation">infotainmentInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="interiorColor">interiorColor</span>|None|[Vehicle](#Vehicle) |xml : string |[interiorInformation](#interiorInformation) |
|<span id="interiorInformation">interiorInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="interiorType">interiorType</span>|None|[Vehicle](#Vehicle) |xml : string |[interiorInformation](#interiorInformation) |
|<span id="irdi">irdi</span>|None|[EClassType](#EClassType) |xml : string ||
|<span id="length">length</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="lifetimeInformation">lifetimeInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="lightingInformation">lightingInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="listPrice">listPrice</span>|None||xml : integer |[productionInformation](#productionInformation) |
|<span id="location">location</span>|None|[Vehicle](#Vehicle) |xml : string |[stateInformation](#stateInformation) |
|<span id="manufacturerKeyNumber">manufacturerKeyNumber</span>|None|[Vehicle](#Vehicle) |xml : string |[registrationInformation](#registrationInformation) |
|<span id="maxAxleLoad">maxAxleLoad</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="maxPayload">maxPayload</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="maxSpeed">maxSpeed</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="maxTowingCapacity">maxTowingCapacity</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="mileage">mileage</span>|None|[Vehicle](#Vehicle) |xml : integer |[stateInformation](#stateInformation) |
|<span id="model">model</span>|None|[Vehicle](#Vehicle) |xml : string |[modelInformation](#modelInformation) |
|<span id="modelArchitecture">modelArchitecture</span>|None|[Vehicle](#Vehicle) |xml : string |[modelInformation](#modelInformation) |
|<span id="modelEndOfProduction">modelEndOfProduction</span>|None|[Vehicle](#Vehicle) |xml : date |[modelInformation](#modelInformation) |
|<span id="modelGeneration">modelGeneration</span>|None|[Vehicle](#Vehicle) |xml : integer |[modelInformation](#modelInformation) |
|<span id="modelInformation">modelInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="modelSeries">modelSeries</span>|None|[Vehicle](#Vehicle) |xml : string |[modelInformation](#modelInformation) |
|<span id="modelStartOfProduction">modelStartOfProduction</span>|None|[Vehicle](#Vehicle) |xml : date |[modelInformation](#modelInformation) |
|<span id="modelVariant">modelVariant</span>|None|[Vehicle](#Vehicle) |xml : string |[modelInformation](#modelInformation) |
|<span id="name">name</span>|None||xml : string ||
|<span id="number">number</span>|None||xml : string |[partInformation](#partInformation) |
|<span id="numberOfAirbags">numberOfAirbags</span>|None|[Vehicle](#Vehicle) |xml : integer |[safetyInformation](#safetyInformation) |
|<span id="numberOfAxles">numberOfAxles</span>|None|[Vehicle](#Vehicle) |xml : integer |[chassisInformation](#chassisInformation) |
|<span id="numberOfCylinders">numberOfCylinders</span>|None|[Vehicle](#Vehicle) |xml : integer |[engineInformation](#engineInformation) |
|<span id="numberOfDoors">numberOfDoors</span>|None|[Vehicle](#Vehicle) |xml : integer |[bodyInformation](#bodyInformation) |
|<span id="numberOfDriveAxles">numberOfDriveAxles</span>|None|[Vehicle](#Vehicle) |xml : integer |[chassisInformation](#chassisInformation) |
|<span id="numberOfForwardGears">numberOfForwardGears</span>|None|[Vehicle](#Vehicle) |xml : integer |[powertrainInformation](#powertrainInformation) |
|<span id="numberOfPassengers">numberOfPassengers</span>|None|[Vehicle](#Vehicle) |xml : integer |[interiorInformation](#interiorInformation) |
|<span id="numberOfSeatRows">numberOfSeatRows</span>|None|[Vehicle](#Vehicle) |xml : integer |[interiorInformation](#interiorInformation) |
|<span id="numberOfSeats">numberOfSeats</span>|None|[Vehicle](#Vehicle) |xml : integer |[interiorInformation](#interiorInformation) |
|<span id="numberOfStandingPlaces">numberOfStandingPlaces</span>|None|[Vehicle](#Vehicle) |xml : integer |[interiorInformation](#interiorInformation) |
|<span id="numberOfValves">numberOfValves</span>|None|[Vehicle](#Vehicle) |xml : integer |[engineInformation](#engineInformation) |
|<span id="operatingHours">operatingHours</span>|None|[Vehicle](#Vehicle) |xml : integer |[stateInformation](#stateInformation) |
|<span id="orderDate">orderDate</span>|None||xml : date |[productionInformation](#productionInformation) |
|<span id="partInformation">partInformation</span>|None|[Part](#Part) |||
|<span id="passengerVolume">passengerVolume</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="performanceInformation">performanceInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="powertrainInformation">powertrainInformation</span>|None|[Part](#Part) , [Vehicle](#Vehicle) |||
|<span id="powertrainLayout">powertrainLayout</span>|None|[Vehicle](#Vehicle) |xml : string |[powertrainInformation](#powertrainInformation) |
|<span id="previousVehicleModel">previousVehicleModel</span>|None|[Vehicle](#Vehicle) |xml : string |[modelInformation](#modelInformation) |
|<span id="productionDate">productionDate</span>|None||xml : date |[productionInformation](#productionInformation) |
|<span id="productionInformation">productionInformation</span>|None||||
|<span id="productionYear">productionYear</span>|None||xml : integer |[productionInformation](#productionInformation) |
|<span id="purchaseDate">purchaseDate</span>|None||xml : date |[productionInformation](#productionInformation) |
|<span id="purchasePrice">purchasePrice</span>|None||xml : integer |[productionInformation](#productionInformation) |
|<span id="range">range</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="rangeWltp">rangeWltp</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="rearSpringType">rearSpringType</span>|None|[Vehicle](#Vehicle) |xml : string |[suspensionInformation](#suspensionInformation) |
|<span id="rearSuspension">rearSuspension</span>|None|[Vehicle](#Vehicle) |xml : string |[suspensionInformation](#suspensionInformation) |
|<span id="registrationAuthority">registrationAuthority</span>|None|[Vehicle](#Vehicle) |xml : string |[registrationInformation](#registrationInformation) |
|<span id="registrationDate">registrationDate</span>|None|[Vehicle](#Vehicle) |xml : date |[registrationInformation](#registrationInformation) |
|<span id="registrationInformation">registrationInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="registrationLocation">registrationLocation</span>|None|[Vehicle](#Vehicle) |xml : string |[registrationInformation](#registrationInformation) |
|<span id="registrationOwner">registrationOwner</span>|None|[Vehicle](#Vehicle) |xml : string |[registrationInformation](#registrationInformation) |
|<span id="registrationPlate">registrationPlate</span>|None|[Vehicle](#Vehicle) |xml : string |[registrationInformation](#registrationInformation) |
|<span id="rim">rim</span>|None|[Vehicle](#Vehicle) |xml : string |[suspensionInformation](#suspensionInformation) |
|<span id="roadNoise">roadNoise</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="safetyInformation">safetyInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="specialUsage">specialUsage</span>|None|[Vehicle](#Vehicle) |xml : string ||
|<span id="stateDateTime">stateDateTime</span>|None|[Vehicle](#Vehicle) |xml : dateTime |[stateInformation](#stateInformation) |
|<span id="stateInformation">stateInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="stationaryNoise">stationaryNoise</span>|None|[Vehicle](#Vehicle) |xml : integer |[performanceInformation](#performanceInformation) |
|<span id="steeringType">steeringType</span>|None|[Vehicle](#Vehicle) |xml : string |[powertrainInformation](#powertrainInformation) |
|<span id="steeringWheelPosition">steeringWheelPosition</span>|None|[Vehicle](#Vehicle) |xml : string |[powertrainInformation](#powertrainInformation) |
|<span id="stroke">stroke</span>|None|[Vehicle](#Vehicle) |xml : double |[engineInformation](#engineInformation) |
|<span id="suspensionInformation">suspensionInformation</span>|None|[Part](#Part) , [Vehicle](#Vehicle) |||
|<span id="tire">tire</span>|None|[Vehicle](#Vehicle) |xml : string |[suspensionInformation](#suspensionInformation) |
|<span id="tongueWeight">tongueWeight</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="trailerWeight">trailerWeight</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="transmission">transmission</span>|None|[Vehicle](#Vehicle) |xml : string |[powertrainInformation](#powertrainInformation) |
|<span id="trunkVolume">trunkVolume</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="turningRadius">turningRadius</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="typeCode">typeCode</span>|None|[Vehicle](#Vehicle) |xml : string ||
|<span id="typeCodeNumber">typeCodeNumber</span>|None|[Vehicle](#Vehicle) |xml : string |[registrationInformation](#registrationInformation) |
|<span id="vehicleIdentificationNumber">vehicleIdentificationNumber</span>|None|[Vehicle](#Vehicle) |xml : string ||
|<span id="version">version</span>|None||xml : string |[partInformation](#partInformation) |
|<span id="warrantyInformation">warrantyInformation</span>|None|[Vehicle](#Vehicle) |||
|<span id="warrantyMaxDuration">warrantyMaxDuration</span>|None|[Vehicle](#Vehicle) |xml : integer |[warrantyInformation](#warrantyInformation) |
|<span id="warrantyMaxMileage">warrantyMaxMileage</span>|None|[Vehicle](#Vehicle) |xml : integer |[warrantyInformation](#warrantyInformation) |
|<span id="weight">weight</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="weightTotal">weightTotal</span>|None|[Vehicle](#Vehicle) |xml : double |[cargoInformation](#cargoInformation) |
|<span id="wheelbase">wheelbase</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="width">width</span>|None|[Vehicle](#Vehicle) |xml : double |[bodyInformation](#bodyInformation) |
|<span id="worldManufacturerCountry">worldManufacturerCountry</span>|None|[Vehicle](#Vehicle) |xml : string |[productionInformation](#productionInformation) |
|<span id="worldManufacturerId">worldManufacturerId</span>|None|[Vehicle](#Vehicle) |xml : string |[productionInformation](#productionInformation) |
|<span id="worldManufacturerName">worldManufacturerName</span>|None|[Vehicle](#Vehicle) |xml : string |[productionInformation](#productionInformation) |
|<span id="worldManufacturerRegion">worldManufacturerRegion</span>|None|[Vehicle](#Vehicle) |xml : string |[productionInformation](#productionInformation) |

## Object Properties
  

|Name|Descriptions|Domain|Range|Subproperty of|
| :--- | :--- | :--- | :--- | :--- |
|<span id="eClassType">eClassType</span>|None|[https://w3id.org/catenax/ontology/core#PhysicalObject](#https://w3id.org/catenax/ontology/core#PhysicalObject) |[EClassType](#EClassType) |[describedByConceptualObject](./core_ontology.md#describedByConceptualObject) |
|<span id="hasPart">hasPart</span>|None|[Vehicle](#Vehicle) |[Part](#Part) ||
|<span id="hasSubpart">hasSubpart</span>|None|[Part](#Part) |[Part](#Part) ||
|<span id="isPartOf">isPartOf</span>|None|[Part](#Part) |[Vehicle](#Vehicle) ||
|<span id="isSubpartOf">isSubpartOf</span>|None|[Part](#Part) |[Part](#Part) ||
|<span id="isVariantOf">isVariantOf</span>|None|[Vehicle](#Vehicle) |[VehicleModel](#VehicleModel) |[describedByConceptualObject](./core_ontology.md#describedByConceptualObject) |
|<span id="supplier">supplier</span>|None|[Part](#Part) |http://www.w3.org/2000/01/rdf-schema#Resource ||
|<span id="manufacturer">manufacturer</span>|None|[Vehicle](#Vehicle) |http://www.w3.org/2000/01/rdf-schema#Resource ||
