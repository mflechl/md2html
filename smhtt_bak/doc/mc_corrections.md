# Monte Carlo Corrections

This section is includes analysis-level corrections that are typically derived late in the analysis itself, e.g. trigger efficiency corrections but not jet energy corrections.

**TODO: SECTION TOO BIG? SPLIT IN DIFFERENT FILES?**

## MC Matching

Most corrections depend on the origin of the reconstructed object, e.g. whether it is a true hadronic tau decay, a muon, an electron, or a jet that gives rise to a reconstructed tau. Therefore, we should agree on MC matching recipes early on and make sure this matching information is available for all samples and objects so that the corrections can be applied later on.

The origin of the reconstructed object is taken as the type of gen particle that matches the object most closely in dR. If there is no match within dR<0.2 with any of the first 5 types in the table below, the object is classed as jet/pileup fake. The values correspond to those given in the corresponding sync ntuple branches. See [these slides](https://indico.cern.ch/event/439324/session/19/contribution/19/attachments/1156754/1663275/AdeWit-MCSplitting1809.pdf) for more information.

| Value 	| Type 			| Gen level object properties |
|-------	|------				|-----------------------------|
|1			| Prompt electron	|abs(pdgid)==11, pT>8, status=isPrompt |
|2			| Prompt muon			|abs(pdgid)==13, pT>8, status=isPrompt |
|3			| tau -> e			|abs(pdgid)==11, pT>8, status=isDirectPromptTauDecayProduct |
|4			| tau -> mu			|abs(pdgid)==13, pT>8, status=isDirectPromptTauDecayProduct |
|5			| tau -> tau_h		|Gen-tau jet *(\*)*,    pT>15, status=isPrompt |
|6			| jet/pileup fake | Anything that doesn't fall in any of the above categories |

*(\*) the gen-tau jet is built by summing the p4 of the visible gen tau decay products, excluding electrons and muons*

## Trigger efficiency corrections

## Tau corrections

### $`\tau_h`$ ID efficiency

### $`e/\mu\rightarrow\tau_h`$ fake rate correction

### $`\tau_h`$ energy scale (ES) correction

### $`e/\rightarrow\tau_h`$ fake energy scale (ES) correction

In $`e\tau_h`$ channel, a large amount of electrons are reconstructed as hadronic taus, which even pass the signal quality requirements.
As a consequence, a $`Z\rightarrow ee`$ peak can be seen in the mass-related distributions.
This may lead to a wrong energy scale of this contribution on a level of several percent.
In order to correct for this, a corresponding ES measurement is performed.
A short description of the measurement method is given [here](https://indico.cern.ch/event/637154/contributions/2582501/attachments/1454655/2244586/EtauES_010517_AdeWit.pdf).
The measurement is performed by Olena Hlushchenko for 2017 data/MC.

## Muon corrections

## Electron corrections

## DY Z (pt, mass) corrections

In order to correct for the mis-modelling of Z-boson kinematics in LO DY samples with respect to data, corrections are measured in a $`Z\rightarrow\mu\mu`$ control region binned in reconstructed Z-boson pt and mass.
A corresponding scale factor file is provided by [Alexei Raspereza](../data/dy-reweighting).
Please note, that there is also an additional measurement provided by [Daniel Winterbottom](https://github.com/danielwinterbottom/CorrectionsWorkspace/blob/ic_embed/inputs/DYWeights/zpt_weights_2017_1D.root) which is only Z-boson pt dependent.
To be compared.

These corrections are applied only to samples with Z-boson mass **greater than 50 GeV**.

## MET recoil correction

### Setting up the MET recoil correction interface

```
cd ${CMSSW_BASE}/src
cmsenv
git clone https://github.com/CMS-HTT/RecoilCorrections.git  HTT-utilities/RecoilCorrections
scram b
```

### Applying recoil correction

Recoil corrections should be applied to the Higgs, DY and W+Jets MC samples. Do not apply recoil corrections to the ttbar, single-top and diboson MC samples. Current corrections for 2017 data/MC are provided for PF MET by [Alexei Raspereza](https://github.com/CMS-HTT/RecoilCorrections/blob/master/data/Type1_PFMET_2017.root). See also [here](https://indico.cern.ch/event/762837/contributions/3172618/attachments/1731302/2798220/Recoils_20181010.pdf) for reference.

Here is a C++ recipe:

```c++
// add the header file to your source file
#include "HTT-utilities/RecoilCorrections/interface/RecoilCorrector.h"

// Create instances of class RecoilCorrection and
// load recoil resolution functions before looping over events;
// The path to files is defined relative to ${CMSSW_BASE}/src directory

// use this RooT file when correcting Type I PF MET
RecoilCorrector recoilPFMetCorrector("HTT-utilities/RecoilCorrections/data/TypeIPFMET_2017XXXXXX.root"); // Type I PF MET

// use this RooT file when correcting MVA MET
RecoilCorrector recoilMvaMetCorrector("HTT-utilities/RecoilCorrections/data/MvaMET_2017YYYYYYY.root"); // MVA MET

...

// apply recoil corrections on event-by-event basis (Type I PF MET)
recoilPFMetCorrector.CorrectByMeanResolution(
    pfmet_ex, // uncorrected type I pf met px (float)
    pfmet_ey, // uncorrected type I pf met py (float)
    genPx, // generator Z/W/Higgs px (float)
    genPy, // generator Z/W/Higgs py (float)
    visPx, // generator visible Z/W/Higgs px (float)
    visPy, // generator visible Z/W/Higgs py (float)
    njets,  // number of jets (hadronic jet multiplicity) (int)
    pfmetcorr_ex, // corrected type I pf met px (float)
    pfmetcorr_ey  // corrected type I pf met py (float)
);


// apply recoil corrections on event-by-event basis (MVA MET)
recoilMvaMetCorrector.CorrectByMeanResolution(
    mvamet_ex, // uncorrected mva met px (float)
    mvamet_ey, // uncorrected mva met py (float)
    genPx, // generator Z/W/Higgs px (float)
    genPy, // generator Z/W/Higgs py (float)
    visPx, // generator visible Z/W/Higgs px (float)
    visPy, // generator visible Z/W/Higgs py (float)
    njets,  // number of jets (hadronic jet multiplicity) (int)
    mvametcorr_ex, // corrected mva met px (float)
    mvametcorr_ey  // corrected mva met py (float)
);
```

### Gen boson p4

Use generator particles and their status flags and pdgId to compute Z/W/H 4-momentum at the generator level. Sum up 4-vectors of generator particles that satisfy the following criteria

```c++
(fromHardProcessFinalState && (isMuon || isElectron || isNeutrino))
|| isDirectHardProcessTauDecayProduct)
```

### Visible gen boson p4

Use generator particles and their status flags and pdgId to compute Z/W/H visible 4-momentum at the generator level. Sum up 4-vectors of generator particles that satisfy the following criteria

```c++
(fromHardProcessFinalState && (isMuon || isElectron))
|| (isDirectHardProcessTauDecayProduct && !isNeutrino) )
```

###  Hadronic jet multiplicity

When computing hadronic jet multiplicity (njets) passed as one of the argument to the recoil corrector, count jets that fulfill the following criteria:

```
pT > 30 GeV and
|eta|<4.7 and
loose PF Jet ID and
dR(lepton,jet) > 0.5
```

**Essential point**. In selected W+Jets events one of the leptons is faked by hadronic jet and this jet should be counted as a part of hadronic recoil to the W boson. Therefore, **when processing W+Jets MC sample, increase the number of jets, passed to the recoil corrector, by one.**


## B-tagging scale factors

The recommended jet flavour definition is `hadronFlavour()` as stated [here](https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods#b_tagging_efficiency_in_MC_sampl)

For analyses that use b-jets, b-tag scale factors are applied to the MC samples.
Use the [promote-demote method](https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods#2a_Jet_by_jet_updating_of_the_b) with b-tagged jets from the [DeepCSV discriminator](jet_selection.md) following [these instructions](https://twiki.cern.ch/twiki/bin/view/CMS/BTagCalibration#Using_b_tag_scale_factors_in_you) with the corresponding b-tagging scale factors that are given [here](https://twiki.cern.ch/twiki/pub/CMS/BtagRecommendation94X/DeepCSV_94XSF_V3_B_F.csv).
The b-tagging efficiencies measured in MC are provided by [Olena Hlushchenko](../data/b-tagging-efficiencies) for various b-taggers and their working points.
To be cross-checked by other groups.
For the current setup, please use `tagging_efficiencies_march2018_btageff-all_samp-inc-DeepCSV_medium.root` efficiency file.

* for b & c jets discrimination: "comb" measurement type is used currently
* for light jets discrimination: "incl" measurement type is used currently
* scale factors & efficiencies are computed within a b-jet pt range of [20 GeV, 1000 GeV]

## Pileup reweighting

We follow [this reweighting procedure](https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVPileUpDescription#Reweighting_Method), using the true number of interactions from MC and true number of interactions in data.

### True number of interactions in Monte Carlo

In 2017, due to a bug in the production of the MC samples, the distribution of the number of pileup interactions is *not the same in all MC datasets*. Therefore, a specific distribution must be used for each MC dataset. These distributions were provided by Artur and are available in [data/pileup/pudistributions_mc_2017.root](/data/pileup/pudistributions_mc_2017.root)

to access a given distribution:

```python
from ROOT import TFile
f = TFile('data/pileup/pudistributions_2017.root')
dataset = '/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'
mc_pu_hist = f.Get(dataset.replace('/','#'))
```

**TODO: CROSS-CHECK THE DISTRIBUTIONS FROM ARTUR**

### True number of interactions in data

The distribution of the true number of interactions for data is available in [data/pileup/pileupdistributions\_data\_2017.root](/data/pileup/pudistributions_data_2017.root)


It was obtained by doing:

```
pileupCalc.py --inputLumiJSON  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PileUp/pileup_latest.txt \
--calcMode true --minBiasXsec 69200 --maxPileupBin 200 --numPileupBins 200  \
-i  /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt \
pudistributions_data_2017.root
```

Please note:

* the same lumi json file as [the one used in the analysis](/doc/samples_data.md#luminosity-json-file)
* that we use 200 bins
* the cross-section of 69.2 mb ([more details](https://hypernews.cern.ch/HyperNews/CMS/get/luminosity/767/1.html))
