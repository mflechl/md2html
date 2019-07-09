# MVA MET Uncertainties

 We consider two types of systematic uncertainties affecting MET:

 * uncertainty in the response of hadronic recoil against leptonic system;
 * uncertainty in the resolution of hadronic recoil against leptonic system. 

A dedicated class has to be used to apply shifts to mva MET, reflecting systematic variations in the response and resolution of hadronic recoil. The code is a part of the package [RecoilCorrections](https://github.com/CMS-HTT/RecoilCorrections).

## Setting up the interface to apply MET related systematics uncertainties 

```
cd ${CMSSW_BASE}/src
cmsenv
git clone https://github.com/CMS-HTT/RecoilCorrections.git  HTT-utilities/RecoilCorrections 
scram b 
```

## Applying MET systematic uncertainties

Systematic variations in MET should be applied to all MC samples following an example below.

```c++
#include "HTT-utilities/RecoilCorrections/interface/MEtSys.h"

// Create an instance of class MEtSys. The constructor loads RooT file with uncertainties. 
// The RooT file also contains histograms reflecting  the hadronic recoil response as 
// a function of the leptonic system pT for three types of processes : 
// 1) W+Jets / DY / Higgs 
// 2) dibosons and single-top
// 3) top pair events
// The path to the RooT file is defined relative to the folder
// $CMSSW_BASE/src 
MEtSys metSys("HTT-utilities/RecoilCorrections/data/MEtSys.root");

// example below demonstrates how to apply upward systematic variation in the 
// RESPONSE of hadronic recoil
// to the W+Jets / DY / Higgs MC samples
// Please note that for the Higgs / W / DY samples you have provide 
// as an input the RECOIL CORRECTED MVA Met
metSys.ApplyMEtSys(
mvamet_x,mvamet_y, // (float) mva met, use RECOIL CORRECTED value for the Higgs / DY / W+Jets MC
lepPx,lepPy, // (float) transverse momentum of the full leptonic system
visLepPx,visLepPy, // (float) transverse momentum of the visible leptonic system
njets, // (int) number of jets : pT > 30 GeV, eta<4.7, loose PF JetID
MEtSys::ProcessType::BOSON; // (int) type of process 
MEtSys::SysType::Response, // (int) type of systematic uncertainty
MEtSys::SysShift::Up, // (int) direction of systematic shift
mvamet_scaleUp_x,mvamet_responseUp_y // (float) shifted value of the mva met
);

// when running on diboson or single-top MC samples replace
// argument  MEtSys::ProcessType::BOSON by MEtSys::ProcessType::EWK,
// for the ttbar MC samples use MEtSys::ProcessType::TOP

// for the systematic shifts in hadronic recoil RESOLUTION replace
// argument  MEtSys::SysType::Response by MEtSys::SysType::Resolution

// when applying downward variation use argument
// MEtSys::SysShift::Down 
```

### Gen boson p4

Follow the same procedure as for [recoil corrections](mc_corrections.md#gen-boson-p4).

### Visible gen boson p4

Follow the same procedure as for [recoil corrections](mc_corrections.md#visible-gen-boson-p4).

### Hadronic jet multiplicity

Follow the same procedure as for [recoil corrections](mc_corrections.md#hadronic-jet-multiplicity).

In addition, when processing **diboson, single-top and ttbar** MC samples, check if the tau lepton candidate is faked by the hadronic jet (`gen_match_2 == 6`). If it is the case, increase the number of jets, passed as one of the arguments to the method `MEtSys::ApplyMEtSys()`, by one. In the analysis of the tt channel check the MC matched objects of both tau lepton candidates. If both tau leptons are faked by the hadronic jet (`gen_match_1=6 and gen_match_2=6`), increase the number of jets by two. If only one tau lepton is faked by the hadronic jet, increase the number of jets by one. 


## MVA MET related systematics in statistical inference

For now it is suggested to account for systematic uncertainties in MVA MET using four uncorrelated nuisance parameters, corresponding to

* uncertainty in the RESPONSE of hadronic recoil in Higgs / DY / W+Jets processes
* uncertainty in the RESOLUTION of hadronic recoil in Higgs / DY / W+Jets processes
* uncertainty in the RESPONSE of hadronic recoil in VV / single-top / ttbar processes
* uncertainty in the RESOLUTION of hadronic recoil in VV / single-top / ttbar processes 

Eventually we intend to use 12 nuisance parameters for the MEt related systematics. Each of the nuisance parameters listed above, will be split into three uncorrelated nuisances corresponding to three jet multiplicity bins:

* njets = 0
* njets = 1
* njets ≥ 2 