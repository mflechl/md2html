# Data Samples 

## Analysis of 2017 datasets

[Analysis recipe for 2017 from PdmV](https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2017Analysis)

### Luminosity JSON file

following the [latest announcement](https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/3067.html) we use the following lumi json file: 

```
 /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt
```

The luminosity is computed in the following way (first [install brilcalc](https://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html)): 

```
 brilcalc lumi \
 --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /fb  \
 -i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt
```

The resulting luminosity is **41.529 /fb**.

## List of datasets

| Single electron | Number of events |
|----|----|
| /SingleElectron/Run2017B-31Mar2018-v1/MINIAOD | 60537490 |
| /SingleElectron/Run2017C-31Mar2018-v1/MINIAOD | 136637888 |
| /SingleElectron/Run2017D-31Mar2018-v1/MINIAOD | 51526710 |
| /SingleElectron/Run2017E-31Mar2018-v1/MINIAOD | 102121689 |
| /SingleElectron/Run2017F-31Mar2018-v1/MINIAOD | 128467223 |

| Single muon | Number of events |
|----|----|
| /SingleMuon/Run2017B-31Mar2018-v1/MINIAOD | 136300266 |
| /SingleMuon/Run2017C-31Mar2018-v1/MINIAOD | 165652756 |
| /SingleMuon/Run2017D-31Mar2018-v1/MINIAOD | 70361660 |
| /SingleMuon/Run2017E-31Mar2018-v1/MINIAOD | 154630534 |
| /SingleMuon/Run2017F-31Mar2018-v1/MINIAOD | 242135500 |

| Tau | Number of events |
|----|----|
| /Tau/Run2017B-31Mar2018-v1/MINIAOD | 38158216 |
| /Tau/Run2017C-31Mar2018-v1/MINIAOD | 55416425 |
| /Tau/Run2017D-31Mar2018-v1/MINIAOD | 20530776 |
| /Tau/Run2017E-31Mar2018-v1/MINIAOD | 44318231 |
| /Tau/Run2017F-31Mar2018-v1/MINIAOD | 88506372 |

| MuonEG | Number of events |
|----|----|
| /MuonEG/Run2017B-31Mar2018-v1/MINIAOD | 4453465 |
| /MuonEG/Run2017C-31Mar2018-v1/MINIAOD | 15595214 |
| /MuonEG/Run2017D-31Mar2018-v1/MINIAOD | 9164365 |
| /MuonEG/Run2017E-31Mar2018-v1/MINIAOD | 19043421 |
| /MuonEG/Run2017F-31Mar2018-v1/MINIAOD | 25776363 |