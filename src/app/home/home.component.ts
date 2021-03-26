import { Component, OnInit ,ElementRef, ViewChild} from '@angular/core';
import { AutoMsgService } from '../services/auto-msg/auto-msg.service';
import { ManualMsgService } from '../services/manual-msg/manual-msg.service';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import {FormControl} from '@angular/forms';
import {MatAutocompleteSelectedEvent, MatAutocomplete} from '@angular/material/autocomplete';
import {MatChipInputEvent} from '@angular/material/chips';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  visible = true;
  selectable = true;
  removable = true;
  separatorKeysCodes: number[] = [ENTER, COMMA];
  fieldCtrl = new FormControl();
  filteredFields: Observable<string[]>;
  public num_msgs;
  public anomaly_percent;
  public pid;
  public fieldvalid=false;
  public stopresponse;
  public params = new Set();
  public MSG_FORMAT = {
    // "@timestamp" ,
    "OPC" : "",
    "DPC" : "",
    // "OTID" : "",
    // "DTID" : "",
    // "TCAP" : "",
    "OPCODE" : "",
    "CDTT" : "",
    "CDNP" : "",
    "CDNAI" : "",
    "CDADDR" : "",
    "CDCN" : "",
    "CDLOC" : "",
    "CGTT" : "",
    "CGNP" : "",
    "CGNAI" : "",
    "CGADDR" : "",
    "CGCN" : "",
    "CgLOC" : "",
    "ATYPE" : "",
    "ASUBTYPE" : "",
    "LSET" : "",
    "CLSF" : "",
    "CAT" : "",
    "MSISDN" : "",
    "IMSI" : "",
    "CLLI": "" ,
    "SameCountryCode" : ""
  }
  fields=["OPC" ,
  "DPC" ,
  "CDTT" ,
  "CDNP" ,
  "CDNAI" ,
  "CDADDR" ,
  "CDCN" ,
  "CDLOC" ,
  "CGTT" ,
  "CGNP" ,
  "CGNAI" ,
  "CGADDR" ,
  "CGCN" ,
  "CgLOC" ,
  "ATYPE" ,
  "ASUBTYPE" ,
  "LSET" ,
  "CLSF" ,
  "CAT" ,
  "MSISDN" ,
  "IMSI" ,
  "CLLI" ,
  "SameCountryCode" ]  

  fieldVisiblity ={
    "OPC": false ,
    "DPC": false,
    "CDTT": false ,
    "CDNP": false ,
    "CDNAI": false ,
    "CDADDR": false ,
    "CDCN": false ,
    "CDLOC": false ,
    "CGTT": false ,
    "CGNP": false ,
    "CGNAI": false ,
    "CGADDR": false ,
    "CGCN": false ,
    "CgLOC": false ,
    "ATYPE": false ,
    "ASUBTYPE": false ,
    "LSET": false ,
    "CLSF": false ,
    "CAT": false ,
    "MSISDN": false ,
    "IMSI": false ,
    "CLLI": false ,
    "SameCountryCode": false
  }

  public OPCODE_mapping = {
    "updateLocation": ["CAT_3_2", ["Intercept","Fraud"], ["profileDisclosure","callRedirection","callInterception","smInterception","servUnavail"]],
    "cancelLocation": ["CAT_2_2", ["DOS","Fraud"], ["servUnavail"]],
    "provideRoamingNumber": ["CAT_1_0", ["Tracking","DOS","Spam"], ["depletion"]],
    "insertSubscriberData": ["CAT_2_2", ["Tracking","Intercept","DOS","Fraud"], ["detailGathering","callRedirection","chargingEvasion","callInterception","smInterception","servUnavail"]],
    "deleteSubscriberData": ["CAT_2_2", ["DOS"], ["chargingEvasion"]],
    "sendParameters": ["CAT_1_0", ["Tracking","Intercept"], ["profileDisclosure","cryptRetrieval","callRedirection","callInterception","servUnavail"]],
    "registerSS": ["CAT_1_0", ["Intercept","DOS"], ["callRedirection","servManipulation","callInterception"]],
    "eraseSS": ["CAT_1_0", ["Intercept","DOS"], ["servManipulation"]],
    "activateSS": ["CAT_1_0", ["Intercept","DOS"], ["servManipulation"]],
    "deactivateSS": ["CAT_1_0", ["DOS"], ["servManipulation"]],
    "interrogateSS": ["CAT_1_0", ["DOS"], ["profileDisclosure"]],
    "registerPassword": ["CAT_1_0", ["DOS"], ["servUnavail"]],
    "processUnstructuredSS-Data": ["CAT_1_0", ["DOS"], ["USSDManipulation"]],
    "sendRoutingInfo": ["CAT_1_0", ["Tracking","Spam"], ["IMSIDisclosure","locationDiscovery","networkDisclosure","depletion"]],
    "updateGprsLocation": ["CAT_3_2", ["DOS","Fraud"], ["profileDisclosure","servUnavail"]],
    "mt-forwardSM": ["CAT_3_3", ["Tracking","DOS","Fraud","Spam"], ["SMSmanipulation"]],
    "sendRoutingInfoForSM": ["CAT_3_3", ["Tracking","Intercept","DOS","Fraud","Spam"], ["IMSIDisclosure","networkDisclosure"]],
    "mo-forwardSM": ["CAT_3_1", ["Tracking","Intercept","Fraud","Spam"], ["SMSmanipulation"]],
    "beginSubscriberActivity": ["CAT_3_1", ["Intercept","DOS"], ["USSDManipulation"]],
    "sendIdentification": ["CAT_1_0", ["Intercept"], ["cryptRetrieval"]],
    "sendAuthenticationInfo": ["CAT_3_2", ["Intercept"], ["cryptRetrieval"]],
    "restoreData": ["CAT_3_1", ["Intercept","DOS","Fraud"], ["profileDisclosure"]],
    "sendIMSI": ["CAT_1_0", ["Tracking","Intercept","DOS","Fraud","Spam"], ["IMSIDisclosure"]],
    "processUnstructuredSS-Request": ["CAT_1_0", ["DOS"], ["USSDManipulation"]],
    "unstructuredSS-Request": ["CAT_1_0", ["Spam"], ["USSDManipulation"]],
    "unstructuredSS-Notify": ["CAT_1_0", ["Spam"], ["USSDManipulation"]],
    "anyTimeModification": ["CAT_1_0", ["Intercept","DOS"], ["callRedirection","chargingEvasion","callInterception","servUnavail"]], 
    "purgeMS": ["CAT_3_1", ["DOS"], ["servUnavail"]],  
    "provideSubscriberInfo": ["CAT_2_1", ["Tracking","Spam"], ["locationDiscovery"]],  
    "anyTimeInterrogation": ["CAT_1_0", ["Tracking","Spam"], ["locationDiscovery","networkDisclosure"]],  
    "provideSubscriberLocation": ["CAT_2_1", ["Tracking","Spam"], ["locationDiscovery"]],  
    "sendRoutingInfoForLCS": ["CAT_1_0", ["Tracking","Spam"], ["IMSIDisclosure"]],  
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

  public progress = false;
  public msggenerate = false;
  public stopmsg = false;
  public manualmsg;

  @ViewChild('fieldInput') fieldInput: ElementRef<HTMLInputElement>;
  @ViewChild('auto') matAutocomplete: MatAutocomplete;

  constructor(private automsgService: AutoMsgService, private manualmsgService: ManualMsgService) {
    this.filteredFields = this.fieldCtrl.valueChanges.pipe(
      startWith(null),
      map((field: string | null) => field ? this._filter(field) : this.fields.slice()));
   }

  ngOnInit(): void {
  }
 

  add(event: MatChipInputEvent): void {
    const input = event.input;
    const value = event.value;
    console.log("value")
    // Add our fruit
    if ((value || '').trim()) {
      this.params.add(value.trim());
      this.fieldVisiblity[value]=true;
      console.log( this.fieldVisiblity[value])
    }

    // Reset the input value
    if (input) {
      input.value = '';
    }

    this.fieldCtrl.setValue(null);
  }

  remove(field: string): void {
    const index = this.params.delete(field);
    this.fieldVisiblity[field]=false;
  }

  selected(event: MatAutocompleteSelectedEvent): void {
    this.params.add(event.option.viewValue);
    this.fieldVisiblity[event.option.viewValue]=true;
    this.fieldInput.nativeElement.value = '';
    this.fieldCtrl.setValue(null);
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.fields.filter(fruit => fruit.toLowerCase().indexOf(filterValue) === 0);
  }


  public valid(){
    if(this.num_msgs!= undefined && this.anomaly_percent!= undefined && this.anomaly_percent >= 0 && this.anomaly_percent <=100){
      // console.log("check in progress")
      this.fieldvalid=true;
    }
    else{
      this.fieldvalid=false;
    }
    console.log(this.fieldvalid)
  }

  public generate() {
    var data = {
      "msgs": this.num_msgs,
      "anomaly": this.anomaly_percent != undefined ? this.anomaly_percent : 0
    }
    console.log(data)
    this.automsgService.generatemsgs(data).subscribe(res => {
      if (res["status"] == "started") {
        this.progress = true;
        this.msggenerate = true;
        this.pid = res["process_id"];
        console.log(res)
      }
    })
  }

  public stop() {
    var data = {
      "pid": this.pid
    }
    this.automsgService.stopmsgs(data).subscribe(res => {
      this.progress = false;
      this.msggenerate = false;
      if (res["status"] == "stopped") {
        this.stopresponse = res["message"];
        setTimeout(() => {
          this.stopmsg = false;
        }, 3000);
      }
      this.stopmsg = true;
    })
  }


  public manual() {
    console.log(this.MSG_FORMAT)
    if(this.MSG_FORMAT['OPCODE'] != ""){
      this.MSG_FORMAT['CAT']=this.MSG_FORMAT['CAT']!=""?this.MSG_FORMAT['CAT']:this.OPCODE_mapping[this.MSG_FORMAT['OPCODE']][0];
      this.MSG_FORMAT['ATYPE']=this.MSG_FORMAT['ATYPE']!=""?this.MSG_FORMAT['ATYPE']:this.OPCODE_mapping[this.MSG_FORMAT['OPCODE']][1];
      this.MSG_FORMAT['ASUBTYPE']=this.MSG_FORMAT['ASUBTYPE']!=null?this.MSG_FORMAT['ASUBTYPE']:this.OPCODE_mapping[this.MSG_FORMAT['OPCODE']][2];
    }
    // console.log(this.MSG_FORMAT)
    this.manualmsgService.manualmsgs(this.MSG_FORMAT).subscribe(res => {
      this.manualmsg=res["result"].toString();
      var doc=document.getElementById("resmsg");
      this.manualmsg=this.manualmsg.replace(/}/g ,"<br>}");
      this.manualmsg=this.manualmsg.replace(/{/g ,"{<br>&ensp;");
      // 
      // this.manualmsg=this.manualmsg.replace(/], /g ,"],<br>&ensp;");
      this.manualmsg=this.manualmsg.replace(/, /g ,",<br>&ensp;");
      doc.innerHTML=this.manualmsg;
      console.log(this.manualmsg)
    })
  }


}
