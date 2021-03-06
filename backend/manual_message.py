import json
import sys
import random
import datetime
import subprocess


MSG_FORMAT = {
    "@timestamp": "",
    "OPC": "",
    "DPC": "",
    "OPCODE": "",
    "CDTT": "",
    "CDNP": "",
    "CDNAI": "",
    "CDADDR": "",
    "CDCN": "",
    "CDLOC": "",
    "CGTT": "",
    "CGNP": "",
    "CGNAI": "",
    "CGADDR": "",
    "CGCN": "",
    "CgLOC": "",
    "ATYPE": "",
    "ASUBTYPE": "",
    "LSET": "",
    "CLSF": "",
    "CAT": "",
    "MSISDN": "",
    "IMSI": "",
    "CLLI": "",
    "SameCountryCode": ""
}

msgfile = sys.argv[1]
with open(msgfile, "r") as tmpfile:
    msg = tmpfile.read()

# cmd="rm -f "+msgfile
cmd = "del /f "+msgfile
print(subprocess.getoutput(cmd))
msg = json.loads(msg)
FILENAME = "manualmessage.json"

# originating point code
OPC_VALUE = ["1-35-1", "7-1-6", "2-2-2", "3-1-6", "6-45-4", "2-105-7", "1-5-7"]

# Destination Point code
DPC_VALUE = ["2-3-4", "3-111-1", "5-5-5",
             "2-1-1", "7-15-4", "4-19-3", "5-6-7", "3-3-3"]

CDADDR_VALUE = ["2138746420", "4238557203", "9127627629", "9327862992", "9122224545", "5527639269",
                "2118278927", "9868525565", "4563565368", "7173602907", "8010343755", "8001434577", "6798289782", "2134893789"]

CDADDR_INVALID_VALUE = ["3124532108", "2937452019",
                        "7119036475", "5891204352", "7823073829"]

CGADDR_VALUE = ["2138746420", "4238557203", "9127627629", "9327862992", "9122224545", "5527639269",
                "2118278927", "9868525565", "4563565368", "7173602907", "8010343755", "8001434577", "6798289782", "2134893789"]

CGADDR_INVALID_VALUE = ["3124532108", "2937452019",
                        "7119036475", "5891204352", "7823073829"]

# Called Country
# CDCN_VALUE = ["Greece", "Netherlands", "Belgium", "France", "Andorra", "Spain", "Hungary", "Bosnia and Herzegovina", "Croatia", "Italy", "Romania", "Switzerland", "Czech Republic", "Slovakia", "Austria", "United Kingdom", "Denmark", "Sweden", "Norway", "Finland", "Lithuania", "Latvia", "Estonia", "Russia", "Ukraine", "Belarus", "Poland", "Germany", "Portugal", "Luxembourg", "Ireland", "Iceland", "Albania", "Cyprus", "Georgia", "Armenia", "Bulgaria", "Turkey", "Slovenia", "Montenegro", "Canada", "United States", "Mexico", "Jamaica", "Barbados", "Saint Lucia", "Bahamas", "Dominica", "Cuba", "Dominican Republic", "Haiti", "Azerbaijan", "Kazakhstan", "Bhutan", "India", "Pakistan", "Afghanistan", "Sri Lanka", "Lebanon", "Jordan", "Iraq", "Kuwait", "Saudi Arabia", "Oman", "United Arab Emirates", "Israel", "Bahrain", "Qatar", "Mongolia", "Nepal", "Uzbekistan", "Tajikistan", "Kyrgyzstan", "Turkmenistan", "Japan", "Vietnam", "Hong Kong", "Cambodia", "China", "Bangladesh",
#               "Malaysia", "Australia", "Indonesia", "Philippines", "Thailand", "Singapore", "Brunei Darussalam", "New Zealand", "Papua New Guinea", "Solomon Islands", "Vanuatu", "Fiji", "Egypt", "Algeria", "Morocco", "Tunisia", "Gambia", "Senegal", "Mauritania", "Mali", "Guinea", "Burkina Faso", "Niger", "Togo", "Benin", "Mauritius", "Liberia", "Sierra Leone", "Ghana", "Nigeria", "Chad", "Central African Republic", "Cameroon", "Cape Verde", "Equatorial Guinea", "Gabon", "Congo", "Democratic Republic of the Congo", "Angola", "Guinea-Bissau", "Sudan", "Ethiopia", "Somalia", "Djibouti", "Kenya", "Uganda", "Burundi", "Mozambique", "Zambia", "Madagascar", "Zimbabwe", "Namibia", "Malawi", "Lesotho", "Botswana", "Swaziland", "Comoros", "South Africa", "Eritrea", "Belize", "Guatemala", "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panama", "Peru", "Argentina", "Brazil", "Chile", "Colombia", "Venezuela", "Bolivia", "Guyana", "Ecuador", "Paraguay", "Suriname", "Uruguay"]

CDCN_VALUE = {
    "Greece": "23.77,37.97",
    "Netherlands": "4.90,52.38",
    "Belgium": "4.35,50.85",
    "France": "2.33,48.83",
    "Monaco": "7.42,44.23",
    "Andorra": "1.53,42.52",
    "Spain": "-3.75,40.42",
    "Hungary": "19.08,47.48",
    "Bosnia and Herzegovina": "18.43,43.87",
    "Croatia": "15.97,45.83",
    "Italy": "12.48,41.90",
    "Romania": "26.17,44.45",
    "Switzerland": "7.47,46.95",
    "Czech Republic": "14.37,50.08",
    "Slovakia": "17.12,48.17",
    "Austria": "16.37,48.20",
    "United Kingdom": "-0.08,51.60",
    "Denmark": "12.57,55.68",
    "Sweden": "18.05,59.33",
    "Norway": "10.75,59.92",
    "Finland": "25.05,60.25",
    "Lithuania": "25.32,54.63",
    "Latvia": "24.13,56.88",
    "Estonia": "24.80,59.37",
    "Russia": "38.02,56.25",
    "Ukraine": "30.47,50.50",
    "Belarus": "27.50,53.87",
    "Moldova": "29.43,47.02",
    "Poland": "21.00,52.22",
    "Germany": "13.42,52.50",
    "Portugal": "-9.17,38.70",
    "Luxembourg": "6.15,49.62",
    "Ireland": "-6.25,53.35",
    "Iceland": "-21.95,64.17",
    "Albania": "19.82,41.30",
    "Malta": "14.52,35.90",
    "Cyprus": "33.42,35.17",
    "Georgia": "44.83,41.72",
    "Armenia": "44.52,40.17",
    "Bulgaria": "23.33,42.75",
    "Turkey": "32.90,39.95",
    "San Marino": "12.50,43.92",
    "Slovenia": "14.55,46.07",
    "Macedonia": "21.73,42.83",
    "Liechtenstein": "9.52,47.13",
    "Montenegro": "19.42,42.72",
    "Canada": "-75.70,45.45",
    "United States": "-77.03,40.52",
    "Mexico": "-99.17,19.33",
    "Jamaica": "-76.83,18.00",
    "Barbados": "-59.50,13.08",
    "Antigua and Barbuda": "-61.80,17.33",
    "Grenada": "-62.23,12.08",
    "Saint Kitts and Nevis": "-62.72,17.28",
    "Saint Lucia": "-60.97,14.03",
    "Bahamas": "-77.33,25.08",
    "Dominica": "-61.40,15.33",
    "Cuba": "-82.37,23.13",
    "Dominican Republic": "-70.55,18.80",
    "Haiti": "-72.33,18.67",
    "Azerbaijan": "49.93,40.48",
    "Kazakhstan": "71.50,51.17",
    "Bhutan": "89.75,27.52",
    "India": "77.22,28.62",
    "Pakistan": "73.17,33.67",
    "Afghanistan": "69.18,34.47",
    "Sri Lanka": "80.43,7.53",
    "Myanmar": "96.33,16.75",
    "Lebanon": "35.52,33.88",
    "Jordan": "35.87,31.95",
    "Syria": "36.30,33.50",
    "Iraq": "44.50,33.33",
    "Kuwait": "48.00,29.50",
    "Saudi Arabia": "46.70,24.68",
    "Oman": "58.60,23.62",
    "United Arab Emirates": "54.37,24.47",
    "Israel": "35.20,31.78",
    "Bahrain": "50.50,26.17",
    "Qatar": "51.58,25.25",
    "Mongolia": "107.50,48.47",
    "Nepal": "85.33,27.75",
    "Iran": "51.63,36.13",
    "Uzbekistan": "69.17,41.33",
    "Tajikistan": "68.80,38.55",
    "Kyrgyzstan": "74.77,42.90",
    "Turkmenistan": "57.83,38.00",
    "Japan": "140.08,36.12",
    "South Korea": "126.97,37.52",
    "VietNam": "105.92,21.08",
    "Hong Kong": "114.25,22.47",
    "Macao": "13.90,22.32",
    "Cambodia": "104.92,11.55",
    "Laos": "103.05,18.62",
    "China": "116.33,39.92",
    "Bangladesh": "90.43,23.72",
    "Maldives": "73.47,4.00",
    "Malaysia": "101.68,3.15",
    "Australia": "149.13,35.25",
    "Indonesia": "106.82,6.15",
    "East Timor": "125.57,8.48",
    "Philippines": "121.05,14.67",
    "Thailand": "100.58,13.75",
    "Singapore": "104.28,1.60",
    "Brunei": "115.55,5.50",
    "New Zealand": "174.77,41.32",
    "Papua New Guinea": "147.13,9.40",
    "Tonga": "-174.00,21.17",
    "Solomon Islands": "159.95,9.45",
    "Vanuatu": "168.30,17.75",
    "Fiji": "178.50,18.10",
    "Kiribati": "173.00,1.50",
    "Samoa": "-171.83,13.83",
    "Micronesia": "158.27,7.52",
    "Palau": "134.47,7.33",
    "Tuvalu": "179.22,8.52",
    "Egypt": "31.23,30.02",
    "Algeria": "3.13,36.70",
    "Morocco": "-7.40,34.62",
    "Tunisia": "10.18,36.83",
    "Libya": "13.32,33.47",
    "Gambia": "-16.67,13.47",
    "Senegal": "-17.48,14.57",
    "Mauritania": "57.50,20.17",
    "Mali": "-7.92,12.57",
    "Guinea": "-13.82,9.48",
    "Ivory Coast": "-5.47,7.37",
    "Burkina Faso": "-1.50,12.25",
    "Niger": "2.10,13.45",
    "Togo": "1.33,6.15",
    "Benin": "2.70,6.38",
    "Mauritius": "57.83,20.27",
    "Liberia": "-10.78,6.30",
    "Sierra Leone": "-13.28,8.50",
    "Ghana": "-0.10,5.58",
    "Nigeria": "7.53,9.08",
    "Chad": "14.98,12.17",
    "Central African Republic": "18.58,4.38",
    "Cameroon": "11.58,3.83",
    "Cape Verde": "-23.57,15.03",
    "Sao Tome and Principe": "6.65,0.17",
    "Equatorial Guinea": "8.83,3.75",
    "Gabon": "9.43,0.42",
    "Congo": "15.20,4.15",
    "Democratic Republic of the Congo": "15.25,4.33",
    "Angola": "13.25,8.83",
    "Guinea-Bissau": "-15.75,11.75",
    "Sudan": "32.58,15.52",
    "Rwanda": "30.07,1.98",
    "Ethiopia": "38.70,9.03",
    "Somalia": "45.42,2.03",
    "Djibouti": "42.33,11.13",
    "Kenya": "36.80,1.28",
    "Uganda": "32.50,0.33",
    "Burundi": "29.30,3.27",
    "Mozambique": "32.53,25.97",
    "Zambia": "28.27,15.47",
    "Madagascar": "47.52,18.92",
    "Zimbabwe": "31.03,17.72",
    "Namibia": "17.07,22.58",
    "Malawi": "33.80,14.00",
    "Lesotho": "27.50,29.30",
    "Botswana": "25.95,24.75",
    "Swaziland": "31.10,26.30",
    "Comoros": "43.40,12.18",
    "South Africa": "28.20,25.73",
    "Eritrea": "38.92,15.32",
    "Belize": "-88.50,17.30",
    "Guatemala": "-90.37,14.67",
    "El Salvador": "-89.17,13.67",
    "Honduras": "-87.23,14.08",
    "Nicaragua": "-86.33,12.10",
    "Costa Rica": "-84.03,9.92",
    "Panama": "-79.42,9.00",
    "Peru": "-77.00,12.00",
    "Argentina": "-60.00,36.50",
    "Brazil": "-47.92,15.78",
    "Chile": "-70.67,33.40",
    "Colombia": "-74.00,4.57",
    "Venezuela": "-66.92,10.50",
    "Bolivia": "-68.17,16.33",
    "Guyana": "-58.20,6.83",
    "Ecuador": "-78.58,0.25",
    "Paraguay": "-57.50,25.17",
    "Suriname": "-55.17,5.83",
    "Uruguay": "-56.18,34.83",
    "St. Helena": "-6.17,16.60"
}

CDLOC_VALUE = ["23.77,37.97", "4.90,52.38", "4.35,50.85", "2.33,48.83", "7.42,44.23", "1.53,42.52", "-3.75,40.42", "19.08,47.48", "18.43,43.87", "15.97,45.83", "12.48,41.90", "26.17,44.45", "7.47,46.95", "14.37,50.08", "17.12,48.17", "16.37,48.20", "-0.08,51.60", "12.57,55.68", "18.05,59.33", "10.75,59.92", "25.05,60.25", "25.32,54.63", "24.13,56.88", "24.80,59.37", "38.02,56.25", "30.47,50.50", "27.50,53.87", "21.00,52.22", "13.42,52.50", "-9.17,38.70", "6.15,49.62", "-6.25,53.35", "-21.95,64.17", "19.82,41.30", "14.52,35.90", "33.42,35.17", "44.83,41.72", "44.52,40.17", "23.33,42.75", "32.90,39.95", "12.50,43.92", "14.55,46.07", "9.52,47.13", "19.42,42.72", "-75.70,45.45", "-77.03,40.52", "-99.17,19.33", "-76.83,18.00", "-59.50,13.08", "-61.80,17.33", "-62.23,12.08", "-62.72,17.28", "-60.97,14.03", "-77.33,25.08", "-61.40,15.33", "-82.37,23.13", "-70.55,18.80", "-72.33,18.67", "49.93,40.48", "71.50,51.17", "89.75,27.52", "77.22,28.62", "73.17,33.67", "69.18,34.47", "80.43,7.53", "35.52,33.88", "35.87,31.95", "44.50,33.33", "48.00,29.50", "46.70,24.68", "58.60,23.62", "54.37,24.47", "35.20,31.78", "50.50,26.17", "51.58,25.25", "107.50,48.47", "85.33,27.75", "69.17,41.33", "68.80,38.55", "74.77,42.90", "57.83,38.00", "140.08,36.12", "105.92,21.08", "114.25,22.47", "13.90,22.32", "104.92,11.55", "103.05,18.62", "116.33,39.92", "90.43,23.72",
               "73.47,4.00", "101.68,3.15", "149.13,35.25", "106.82,6.15", "125.57,8.48", "121.05,14.67", "100.58,13.75", "104.28,1.60", "115.55,5.50", "174.77,41.32", "147.13,9.40", "-174.00,21.17", "159.95,9.45", "168.30,17.75", "178.50,18.10", "173.00,1.50", "-171.83,13.83", "158.27,7.52", "134.47,7.33", "179.22,8.52", "31.23,30.02", "3.13,36.70", "-7.40,34.62", "10.18,36.83", "-16.67,13.47", "-17.48,14.57", "57.50,20.17", "-7.92,12.57", "-13.82,9.48", "-5.47,7.37", "-1.50,12.25", "2.10,13.45", "1.33,6.15", "2.70,6.38", "57.83,20.27", "-10.78,6.30", "-13.28,8.50", "-0.10,5.58", "7.53,9.08", "14.98,12.17", "18.58,4.38", "11.58,3.83", "-23.57,15.03", "6.65,0.17", "8.83,3.75", "9.43,0.42", "15.20,4.15", "15.25,4.33", "13.25,8.83", "-15.75,11.75", "32.58,15.52", "30.07,1.98", "38.70,9.03", "45.42,2.03", "42.33,11.13", "36.80,1.28", "32.50,0.33", "29.30,3.27", "32.53,25.97", "28.27,15.47", "47.52,18.92", "31.03,17.72", "17.07,22.58", "33.80,14.00", "27.50,29.30", "25.95,24.75", "31.10,26.30", "43.40,12.18", "28.20,25.73", "38.92,15.32", "-88.50,17.30", "-90.37,14.67", "-89.17,13.67", "-87.23,14.08", "-86.33,12.10", "-84.03,9.92", "-79.42,9.00", "-77.00,12.00", "-60.00,36.50", "-47.92,15.78", "-70.67,33.40", "-74.00,4.57", "-66.92,10.50", "-68.17,16.33", "-58.20,6.83", "-78.58,0.25", "-57.50,25.17", "-55.17,5.83", "-56.18,34.83", "-6.17,16.60"]

MSISDN_VALUE = ["2138746420", "4238557203", "9127627629", "9327862992", "9122224545", "5527639269",
                "2118278927", "9868525565", "4563565368", "7173602907", "8010343755", "8001434577", "6798289782", "2134893789"]


IMSI_VALUE = ["2138746420", "4238557203", "9127627629", "9327862992", "9122224545", "5527639269", "2118278927",
              "9868525565", "4563565368", "7173602907", "8010343755", "8001434577", "6798289782", "2134893789"]

# Supported Link values
LINK_VALUE = ["LS1", "LS2", "LS3", "LS4",
              "LS5", "LS6", "LS7", "LS8", "LS9", "LS10"]

# Category 2 Messages Division
CLASSIFICATION_VALUE = ["Inroamer", "Home Network"]

OPCODE_VALUE = ["updateLocation", "provideRoamingNumber", "noteSubscriberDataModified", "resumeCallHandling", "insertSubscriberData", "sendParameters", "registerSS", "eraseSS", "activateSS", "deactivateSS", "interrogateSS", "authenticationFailureReport", "notifySS", "registerPassword", "getPassword", "processUnstructuredSS-Data", "releaseResources", "mt-ForwardSM-VGCS", "sendRoutingInfo", "updateGprsLocation", "sendRoutingInfoForGprs", "failureReport", "noteMsPresentForGprs", "performHandover", "sendEndSignal", "performSubsequentHandover", "provideSIWFSNumber", "siwfs-SignallingModify", "processAccessSignalling", "forwardAccessSignalling", "noteInternalHandover", "forwardCheckSsIndication", "prepareGroupCall", "sendGroupCallEndSignal",
                "processGroupCallSignalling", "forwardGroupCallSignalling", "checkIMEI", "mt-forwardSM", "sendRoutingInfoForSM", "mo-forwardSM", "reportSmDeliveryStatus", "noteSubscriberPresent", "traceSubscriberActivity", "updateVcsgLocation", "beginSubscriberActivity", "sendIdentification", "sendAuthenticationInfo", "restoreData", "sendIMSI", "processUnstructuredSS-Request", "unstructuredSS-Request", "unstructuredSS-Notify", "anyTimeSubscriptionInterrogation", "anyTimeModification", "readyForSM", "purgeMS", "prepareHandover", "prepareSubsequentHandover", "anyTimeInterrogation", "ss-Invocation-Notification", "registerCC-Entry", "eraseCC-Entry", "secureTransportClass1", "secureTransportClass2", "secureTransportClass3", "secureTransportClass4"]
OPCODE_mapping = {
    "updateLocation": ["CAT_3_2", ["Intercept", "Fraud"], ["profileDisclosure", "callRedirection", "callInterception", "smInterception", "servUnavail"]],
    "cancelLocation": ["CAT_2_2", ["DOS", "Fraud"], ["servUnavail"]],
    "provideRoamingNumber": ["CAT_1_0", ["Tracking", "DOS", "Spam"], ["depletion"]],
    "insertSubscriberData": ["CAT_2_2", ["Tracking", "Intercept", "DOS", "Fraud"], ["detailGathering", "callRedirection", "chargingEvasion", "callInterception", "smInterception", "servUnavail"]],
    "deleteSubscriberData": ["CAT_2_2", ["DOS"], ["chargingEvasion"]],
    "sendParameters": ["CAT_1_0", ["Tracking", "Intercept"], ["profileDisclosure", "cryptRetrieval", "callRedirection", "callInterception", "servUnavail"]],
    "registerSS": ["CAT_1_0", ["Intercept", "DOS"], ["callRedirection", "servManipulation", "callInterception"]],
    "eraseSS": ["CAT_1_0", ["Intercept", "DOS"], ["servManipulation"]],
    "activateSS": ["CAT_1_0", ["Intercept", "DOS"], ["servManipulation"]],
    "deactivateSS": ["CAT_1_0", ["DOS"], ["servManipulation"]],
    "interrogateSS": ["CAT_1_0", ["DOS"], ["profileDisclosure"]],
    "registerPassword": ["CAT_1_0", ["DOS"], ["servUnavail"]],
    "processUnstructuredSS-Data": ["CAT_1_0", ["DOS"], ["USSDManipulation"]],
    "sendRoutingInfo": ["CAT_1_0", ["Tracking", "Spam"], ["IMSIDisclosure", "locationDiscovery", "networkDisclosure", "depletion"]],
    "updateGprsLocation": ["CAT_3_2", ["DOS", "Fraud"], ["profileDisclosure", "servUnavail"]],
    "mt-forwardSM": ["CAT_3_3", ["Tracking", "DOS", "Fraud", "Spam"], ["SMSmanipulation"]],
    "sendRoutingInfoForSM": ["CAT_3_3", ["Tracking", "Intercept", "DOS", "Fraud", "Spam"], ["IMSIDisclosure", "networkDisclosure"]],
    "mo-forwardSM": ["CAT_3_1", ["Tracking", "Intercept", "Fraud", "Spam"], ["SMSmanipulation"]],
    "beginSubscriberActivity": ["CAT_3_1", ["Intercept", "DOS"], ["USSDManipulation"]],
    "sendIdentification": ["CAT_1_0", ["Intercept"], ["cryptRetrieval"]],
    "sendAuthenticationInfo": ["CAT_3_2", ["Intercept"], ["cryptRetrieval"]],
    "restoreData": ["CAT_3_1", ["Intercept", "DOS", "Fraud"], ["profileDisclosure"]],
    "sendIMSI": ["CAT_1_0", ["Tracking", "Intercept", "DOS", "Fraud", "Spam"], ["IMSIDisclosure"]],
    "processUnstructuredSS-Request": ["CAT_1_0", ["DOS"], ["USSDManipulation"]],
    "unstructuredSS-Request": ["CAT_1_0", ["Spam"], ["USSDManipulation"]],
    "unstructuredSS-Notify": ["CAT_1_0", ["Spam"], ["USSDManipulation"]],
    "anyTimeModification": ["CAT_1_0", ["Intercept", "DOS"], ["callRedirection", "chargingEvasion", "callInterception", "servUnavail"]],
    "purgeMS": ["CAT_3_1", ["DOS"], ["servUnavail"]],
    "provideSubscriberInfo": ["CAT_2_1", ["Tracking", "Spam"], ["locationDiscovery"]],
    "anyTimeInterrogation": ["CAT_1_0", ["Tracking", "Spam"], ["locationDiscovery", "networkDisclosure"]],
    "provideSubscriberLocation": ["CAT_2_1", ["Tracking", "Spam"], ["locationDiscovery"]],
    "sendRoutingInfoForLCS": ["CAT_1_0", ["Tracking", "Spam"], ["IMSIDisclosure"]],
    "subscriberLocationReport": ["CAT_1_0", ["Tracking"], ["eventspoofing"]],
    "NoteMM-Event": ["CAT_3_1", ["Tracking"], ["eventspoofing"]],
    'noteSubscriberDataModified': ['CAT_1_0', 'null', 'null'],
    'resumeCallHandling': ['CAT_1_0', 'null', 'null'],
    'authenticationFailureReport': ['CAT_3_1', 'null', 'null'],
    'notifySS': ['CAT_1_0', 'null', 'null'],
    'releaseResources': ['CAT_1_0', 'null', 'null'],
    'mt-ForwardSM-VGCS  ': ['CAT_1_0', 'null', 'null'],
    'failureReport': ['CAT_1_0', 'null', 'null'],
    'noteMsPresentForGprs': ['CAT_1_0', 'null', 'null'],
    'performHandover': ['CAT_1_0', 'null', 'null'],
    'sendEndSignal': ['CAT_1_0', 'null', 'null'],
    'performSubsequentHandover': ['CAT_1_0', 'null', 'null'],
    'provideSIWFSNumber': ['CAT_1_0', 'null', 'null'],
    'siwfs-SignallingModify': ['CAT_1_0', 'null', 'null'],
    'processAccessSignalling': ['CAT_1_0', 'null', 'null'],
    'forwardAccessSignalling': ['CAT_1_0', 'null', 'null'],
    'noteInternalHandover': ['CAT_1_0', 'null', 'null'],
    'cancelVcsgLocation': ['CAT_2_2', 'null', 'null'],
    'forwardCheckSsIndication': ['CAT_1_0', 'null', 'null'],
    'prepareGroupCall': ['CAT_1_0', 'null', 'null'],
    'sendGroupCallEndSignal': ['CAT_1_0', 'null', 'null'],
    'processGroupCallSignalling': ['CAT_1_0', 'null', 'null'],
    'forwardGroupCallSignalling': ['CAT_1_0', 'null', 'null'],
    'checkIMEI': ['CAT_1_0', 'null', 'null'],
    'noteSubscriberPresent': ['CAT_3_1', 'null', 'null'],
    'alertServiceCentreWithoutResult': ['CAT_2_2', 'null', 'null'],
    'activateTraceMode': ['CAT_2_2', 'null', 'null'],
    'deactivateTraceMode': ['CAT_2_2', 'null', 'null'],
    'traceSubscriberActivity': ['CAT_1_0', 'null', 'null'],
    'updateVcsgLocation  ': ['CAT_3_2', 'null', 'null'],
    'anyTimeSubscriptionInterrogation': ['CAT_1_0', 'null', 'null'],
    'informServiceCentre': ['CAT_2_2', 'null', 'null'],
    'alertServiceCentre': ['CAT_2_2', 'null', 'null'],
    'readyForSM': ['CAT_1_0', 'null', 'null'],
    'prepareHandover': ['CAT_1_0', 'null', 'null'],
    'prepareSubsequentHandover': ['CAT_1_0', 'null', 'null'],
    'ss-Invocation-Notification': ['CAT_1_0', 'null', 'null'],
    'setReportingState': ['CAT_2_2', 'null', 'null'],
    'statusReport': ['null', 'null', 'null'],
    'remoteUserFree': ['CAT_2_2', 'null', 'null'],
    'registerCC-Entry': ['CAT_1_0', 'null', 'null'],
    'eraseCC-Entry': ['CAT_1_0', 'null', 'null'],
    'secureTransportClass1': ['CAT_1_0', 'null', 'null'],
    'secureTransportClass2': ['CAT_1_0', 'null', 'null'],
    'secureTransportClass3': ['CAT_1_0', 'null', 'null'],
    'secureTransportClass4': ['CAT_1_0', 'null', 'null'],
    'sendGroupCallInfo': ['CAT_1_0', 'null', 'null'],
    'istAlert': ['CAT_3_1', 'null', 'null'],
    'istCommand': ['CAT_2_2', 'null', 'null']
}
INVALID_OPCODE_VALUE = ["cancelVcsgLocation", "reset", "setReportingState", "statusReport", "remoteUserFree", "istCommand",
                        "alertServiceCentre", "informServiceCentre", "activateTraceMode", "deactivateTraceMode", "deleteSubscriberData"]

CAT_VALUE = ["cat3.2", "cat1", "cat1", "cat1", "cat2", "cat1", "cat1", "cat1", "cat1", "cat2", "cat1", "cat3.1", "cat1", "cat1", "cat2", "cat1", "cat1", "cat1", "cat1", "cat3.2", "cat1", "cat2", "cat1", "cat1", "cat1", "cat1", "cat1", "cat2", "cat1", "cat1", "cat1", "cat1", "cat1", "cat1", "cat1", "cat1",
             "cat2", "cat3.3", "cat3.3", "cat3.1", "cat3.3", "cat3.1", "cat1", "cat3.2", "cat3.1", "cat2", "cat3.2", "cat3.1", "cat1", "cat1", "cat1", "cat2", "cat1", "cat1", "cat2", "cat3.1", "cat1", "cat1", "cat1", "cat1", "cat1", "cat1", "cat2", "cat1", "cat1", "cat1", "cat1", "cat2", "cat1", "cat3.1", "cat3.1"]

ATYPE_VALUE = ["['intercept','fraud']", "['tracking','DOS','spam']", "[]", "[]", "[]", "['tracking','intercept']", "['intercept','DOS']", "['intercept','DOS']", "['intercept','DOS']", "['DOS']", "['DOS']", "[]", "[]", "['DOS']", "['DOS']", "['DOS']", "[]", "[]", "['tracking','spam']", "['DOS','fraud']", "['tracking','spam']", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "['tracking','DOS','fraud','spam']",
               "['tracking','intercept','DOS','fraud','spam']", "['tracking','intercept','fraud','spam']", "['DOS']", "[]", "[]", "[]", "['intercept','DOS']", "['intercept']", "['intercept']", "['intercept','DOS','fraud']", "['tracking','intercept','DOS','fraud','spam']", "['DOS']", "['spam']", "['spam']", "[]", "['intercept','DOS']", "[]", "['DOS']", "[]", "[]", "['tracking']", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "['tracking','spam']", "['tracking']", "[]", "['tracking']"]

ASUBTYPE_VALUE = ["['profileDisclosure','callRedirection','callInterception','smInterception','servUnavail']", "['depletion']", "[]", "[]", "[]", "['profileDisclosure','cryptRetrieval','callRedirection','callInterception','servUnavail']", "['callRedirection','servManipulation','callInterception']", "['servManipulation']", "['servManipulation']", "['servManipulation']", "['profileDisclosure']", "[]", "[]", "['servUnavail']", "[]", "['USSDManipulation','spoofing']", "[]", "[]", "['IMSIDisclosure','locationDiscovery','networkDisclosure']", "['profileDisclosure','servUnavail']", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                  "[]", "[]", "[]", "[]", "[]", "[]", "[]", "['spoofing']", "['IMSIDisclosure','networkDisclosure']", "['spoofing']", "[]", "[]", "[]", "[]", "['USSDManipulation']", "['cryptRetrieval']", "['cryptRetrieval']", "['profileDisclosure']", "['IMSIDisclosure']", "['USSDManipulation','spoofing']", "['USSDManipulation','spoofing']", "['USSDManipulation','spoofing']", "[]", "['callRedirection','chargingEvasion','callInterception','servUnavail']", "[]", "['servUnavail']", "[]", "[]", "['locationDiscovery','networkDisclosure']", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "['IMSIDisclosure']", "['spoofing']", "[]", "['eventspoofing']"]

RAND_OPC = random.randint(0, 32767) % len(OPC_VALUE)
RAND_DPC = random.randint(0, 32767) % len(DPC_VALUE)
RAND_LS = random.randint(0, 32767) % len(LINK_VALUE)
RAND_CDCN = random.choice(list(CDCN_VALUE.keys()))
RAND_CDADDR = random.randint(0, 32767) % len(CDADDR_VALUE)
RAND_CGADDR = random.randint(0, 32767) % len(CDADDR_VALUE)
RAND_CDTT = random.randint(0, 32767) % 255
RAND_CDNP = random.randint(0, 32767) % 7
RAND_CDNAI = random.randint(0, 32767) % 4
RAND_CGCN = random.choice(list(CDCN_VALUE.keys()))
RAND_CGTT = random.randint(0, 32767) % 255
RAND_CGNP = random.randint(0, 32767) % 7
RAND_CGNAI = random.randint(0, 32767) % 4
RAND_MSISDN = random.randint(0, 32767) % len(MSISDN_VALUE)
RAND_IMSI = random.randint(0, 32767) % len(IMSI_VALUE)
RAND_OPCODE = random.choice(list(OPCODE_mapping.keys()))
date = datetime.datetime.now()
date = date.strftime("%FT%T.%f")[:-3]+"Z"

# CDCN and CGCN should always be different
while (RAND_CDCN == RAND_CGCN):
    RAND_CGCN = random.choice(list(CDCN_VALUE.keys()))

# Generate the One random message(in JSON format) according to above rules.
MSG = {
    "@timestamp": date,
    "OPC": OPC_VALUE[RAND_OPC],
    "DPC": DPC_VALUE[RAND_DPC],
    "OPCODE": RAND_OPCODE if msg['OPCODE'] == "" else msg['OPCODE'],
    "CDTT": RAND_CDTT,
    "CDNP": RAND_CDNP,
    "CDNAI": RAND_CDNAI,
    "CDADDR": CDADDR_VALUE[RAND_CDADDR] if msg['CDADDR'] == "" else msg['CDADDR'],
    "CDCN": RAND_CDCN,
    "CDLOC": CDCN_VALUE[RAND_CDCN],
    "CGTT": RAND_CGTT,
    "CGNP": RAND_CGNP,
    "CGNAI": RAND_CGNAI,
    "CGADDR": CGADDR_VALUE[RAND_CGADDR] if msg['CGADDR'] == "" else msg['CGADDR'],
    "CGCN": RAND_CGCN,
    "CgLOC": CDCN_VALUE[RAND_CGCN],
    # OPCODE  -------------------
    "ATYPE": OPCODE_mapping[RAND_OPCODE][1] if msg['ATYPE'] == "" else msg['ATYPE'],
    # OPCODE  -------------------
    "ASUBTYPE": OPCODE_mapping[RAND_OPCODE][2] if msg['ASUBTYPE'] == "" else msg['ASUBTYPE'],
    "LSET": LINK_VALUE[RAND_LS] if msg['LSET'] == "" else msg['LSET'],
    "CLSF": "unknown",
    # OPCODE  -------------------
    "CAT": OPCODE_mapping[RAND_OPCODE][0] if msg['CAT'] == "" else msg['CAT'],
    "MSISDN": MSISDN_VALUE[RAND_MSISDN],
    "IMSI": IMSI_VALUE[RAND_IMSI],
    "CLLI": "tklc1111101",
    "SameCountryCode": "0"
}
with open(FILENAME, "w") as tmpfile:
    tmpfile.write(str(MSG)+"\n")
