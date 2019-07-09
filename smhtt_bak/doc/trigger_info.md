# Trigger Information

## Important remarks

* Note that currently many triggers have been listed for the MC for the sake of completion - probably more than would actually be needed for the analysis, depending on prescales in the data and the acceptance for signal.
* **The HLT menu used in the v2 MC production is ..... (TODO UPDATE MENU)** You can [browse the configuration](https://cmsweb-testbed.cern.ch/confdb/)
* The filter labels and L1 seeds can be extracted using the hltConfigFromDB tool in CMSSW, e.g. (**TODO COMMAND DOES NOT WORK**):
```
hltConfigFromDB --configName /frozen/2016/25ns10e33/v2.1/HLT/V3 --cff --paths HLT\\_Ele23_WPLoose_Gsf_v4 | grep 'EDFilter\|MinN =\|ncandcut\|saveTags\|L1SeedsLogicalExpression''
```
* Please note that you may have to keep the `L1Trigger` objects in your skims and ntuples. When running on MINIAOD, do: 

```
'keep *_caloStage2Digis_*_*',
'keep *_gmtStage2Digis_*_*'
```

* Please do not skim your MC events requiring trigger bits.
* Please remember the following applying trigger matching:
	* Always check if you match to a trigger object passing filter(s) of interest (usually the last filter of a trigger path),
   * Always check type of trigger object (important for filters mixing different types like mu-tau overlap filters). Trigger types are defined in [DataFormats/HLTReco/interface/TriggerTypeDefs.h](http://cmslxr.fnal.gov/source/DataFormats/HLTReco/interface/TriggerTypeDefs.h?v=CMSSW_9_4_2)

## mu tau triggers

### 2017 MC v2 samples
| HLT Path | L1 seed | muon filter to match | tau filter(s) to match | Remarks |
|------------| ----------| -----------------------|--------------------------|------------------------------------------|
| HLT\_IsoMu24\_v | L1_SingleMu22 |hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07 | - | |
| HLT\_IsoMu27\_v | L1\_SingleMu22 OR L1\_SingleMu25  | hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07 | | |
| HLT\_IsoMu20\_eta2p1\_LooseChargedIsoPFTau27\_eta2p1\_CrossL1\_v | L1\_Mu18er2p1\_Tau24er2p1 | hltSelectedPFTau27LooseChargedIsolationAgainstMuonL1HLTMatched AND hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded | hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07 AND hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded | |

### Data
| HLT Path | L1 seed | muon filter to match | tau filter(s) to match | Remarks |
|------------| ----------| -----------------------|--------------------------|-------------------------------|
| HLT\_IsoMu24\_v | L1_SingleMu22  | hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07 | - | Enabled from Run2017F, up to 1.8e34 column (pre-run 305388) / 1.5e34 column (post-run 305388) |
| HLT\_IsoMu27\_v | L1\_SingleMu22 OR L1\_SingleMu25  | hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07 | | |
| HLT\_IsoMu20\_eta2p1\_LooseChargedIsoPFTau27\_eta2p1\_CrossL1\_v | L1\_Mu18er2p1_Tau24er2p1 | hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07 AND hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded | hltSelectedPFTau27LooseChargedIsolationAgainstMuonL1HLTMatched AND hltOverlapFilterIsoMu20LooseChargedIsoPFTau27L1Seeded | |

### Scale factors 

For the purpose of applying trigger SF, the following formula can be used:

**TODO: EQUATIONS NOT CLEAR; WRITE IN LATEX**

```
l = IsoMu20_eta2p1 / tau = LooseChargedIsoPFTau27_eta2p1

L = IsoMu24 OR IsoMu27

Eff(OR all paths) = Eff(L)*(1-Eff(tau)) + Eff(l)*Eff(tau)

SF = Eff(OR data)/Eff(OR MC)
```

## e tau triggers

### 2017 MC v2 samples

| HLT Path | L1 seed | muon filter to match | tau filter(s) to match | Remarks |
|------------| ----------| -----------------------|--------------------------|-------------------------------|
| HLT\_Ele27\_WPTight\_Gsf\_v | L1\_SingleEG24 OR ... OR L1\_SingleEG50 OR L1\_SingleEG34er2p1 OR ... OR L1\_SingleEG38er2p1 OR L1\_SingleIsoEG24er2p1 OR ... OR L1\_SingleIsoEG36er2p1 OR L1\_SingleIsoEG24 OR ... OR L1\_SingleIsoEG38 | hltEle27WPTightGsfTrackIsoFilter | - | |
| HLT\_Ele32\_WPTight\_Gsf\_v | L1\_SingleEG24 OR ... OR L1\_SingleEG50 OR L1\_SingleEG34er2p1 OR ... OR L1\_SingleEG38er2p1 OR L1\_SingleIsoEG24er2p1 OR ... OR L1\_SingleIsoEG36er2p1 OR L1\_SingleIsoEG24 OR ... OR L1\_SingleIsoEG38 | hltEle32WPTightGsfTrackIsoFilter | - | |
| HLT\_Ele35\_WPTight\_Gsf\_v | L1\_SingleEG24 OR ... OR L1\_SingleEG50 OR L1\_SingleEG34er2p1 OR ... OR L1\_SingleEG38er2p1 OR L1\_SingleIsoEG24er2p1 OR ... OR L1\_SingleIsoEG36er2p1 OR L1\_SingleIsoEG24 OR ... OR L1\_SingleIsoEG38 | hltEle35noerWPTightGsfTrackIsoFilter | - | |
| HLT\_Ele24\_eta2p1\_WPTight\_Gsf\_LooseChargedIsoPFTau30\_eta2p1\_CrossL1\_v | L1\_LooseIsoEG22er2p1\_IsoTau26er2p1\_dR\_Min0p3 OR L1\_LooseIsoEG24er2p1\_IsoTau27er2p1\_dR\_Min0p3 |  hltEle24erWPTightGsfTrackIsoFilterForTau AND hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30 | hltSelectedPFTau30LooseChargedIsolationL1HLTMatched AND hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30 | |

### Data

| HLT Path | L1 seed | muon filter to match | tau filter(s) to match | Remarks |
|------------| ----------| -----------------------|--------------------------|-------------------------------|
| HLT\_Ele27\_WPTight\_Gsf\_v | L1\_SingleEG24 OR ... OR L1\_SingleEG50 OR L1\_SingleEG34er2p1 OR ... OR L1\_SingleEG38er2p1 OR L1\_SingleIsoEG24er2p1 OR ... OR L1\_SingleIsoEG36er2p1 OR L1\_SingleIsoEG24 OR ... OR L1\_SingleIsoEG38 | hltEle27WPTightGsfTrackIsoFilter | - | |
| HLT\_Ele32\_WPTight\_Gsf\_v | L1\_SingleEG24 OR ... OR L1\_SingleEG50 OR L1\_SingleEG34er2p1 OR ... OR L1\_SingleEG38er2p1 OR L1\_SingleIsoEG24er2p1 OR ... OR L1\_SingleIsoEG36er2p1 OR L1\_SingleIsoEG24 OR ... OR L1\_SingleIsoEG38 | hltEle32WPTightGsfTrackIsoFilter | - | Included since HLT menu v3 (post-run 302026, ~Run 2017C) |
| HLT\_Ele35\_WPTight\_Gsf\_v | L1\_SingleEG24 OR ... OR L1\_SingleEG50 OR L1\_SingleEG34er2p1 OR ... OR L1\_SingleEG38er2p1 OR L1\_SingleIsoEG24er2p1 OR ... OR L1\_SingleIsoEG36er2p1 OR L1\_SingleIsoEG24 OR ... OR L1\_SingleIsoEG38 | hltEle35noerWPTightGsfTrackIsoFilter | - | |
| HLT\_Ele24\_eta2p1\_WPTight\_Gsf\_LooseChargedIsoPFTau30\_eta2p1\_CrossL1\_v | L1\_LooseIsoEG22er2p1\_IsoTau26er2p1\_dR\_Min0p3 OR L1\_LooseIsoEG24er2p1\_IsoTau27er2p1\_dR\_Min0p3 |  hltEle24erWPTightGsfTrackIsoFilterForTau AND hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30 | hltSelectedPFTau30LooseChargedIsolationL1HLTMatched AND hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30 | |

### Scale factors


For the purpose of applying trigger SF, the following formula can be used:

```
l = Ele24_eta2p1 / tau = LooseChargedIsoPFTau30_eta2p1

L = Ele32 OR Ele35

Eff(OR all paths) = Eff(L)*(1-Eff(tau)) + Eff(l)*Eff(tau)

SF = Eff(OR data)/Eff(OR MC)
```

## tau tau triggers

### 2017 MC v2 samples

| HLT Path | L1 seed | muon filter to match | tau filter(s) to match | Remarks |
|------------| ----------| -----------------------|--------------------------|-------------------------------|
| HLT\_DoubleTightChargedIsoPFTau35\_Trk1\_TightID\_eta2p1\_Reg\_v | L1\_DoubleIsoTau28er2p1 OR ... OR L1\_DoubleIsoTau38er2p1 OR L1\_DoubleTau70er2p1 | hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg |  L1 pT requirement to be tightened to 32 GeV to match lowest enabled L1 seed in data |
| HLT\_DoubleMediumChargedIsoPFTau40\_Trk1\_TightID\_eta2p1\_Reg\_v | L1\_DoubleIsoTau28er2p1 OR ... OR L1\_DoubleIsoTau38er2p1 OR L1\_DoubleTau70er2p1 | hltDoublePFTau40TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg | L1 pT requirement to be tightened to 32 GeV to match lowest enabled L1 seed in data |
| HLT\_DoubleTightChargedIsoPFTau40\_Trk1\_eta2p1\_Reg\_v | L1\_DoubleIsoTau28er2p1 OR ... OR L1\_DoubleIsoTau38er2p1 OR L1\_DoubleTau70er2p1 | hltDoublePFTau40TrackPt1TightChargedIsolationDz02Reg | L1 pT requirement to be tightened to 32 GeV to match lowest enabled L1 seed in data |


### Data

| HLT Path | L1 seed | muon filter to match | tau filter(s) to match | Remarks |
|------------| ----------| -----------------------|--------------------------|-------------------------------|
| HLT\_DoubleTightChargedIsoPFTau35\_Trk1\_TightID\_eta2p1\_Reg\_v | L1\_DoubleIsoTau28er2p1 OR ... OR L1\_DoubleIsoTau38er2p1 OR L1\_DoubleTau70er2p1 | hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg | |
| HLT\_DoubleMediumChargedIsoPFTau40\_Trk1\_TightID\_eta2p1\_Reg\_v | L1\_DoubleIsoTau28er2p1 OR ... OR L1\_DoubleIsoTau38er2p1 OR L1\_DoubleTau70er2p1 | hltDoublePFTau40TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg | |
| HLT\_DoubleTightChargedIsoPFTau40\_Trk1\_eta2p1\_Reg\_v | L1\_DoubleIsoTau28er2p1 OR ... OR L1\_DoubleIsoTau38er2p1 OR L1\_DoubleTau70er2p1 | hltDoublePFTau40TrackPt1TightChargedIsolationDz02Reg | |

## e mu triggers

To be written