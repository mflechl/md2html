# Analysis ntuple

In the past, sync ntuples were only used to synchronize the analysis of the different groups. We now intend to make it possible to use them as well to perform the full analysis, with the following advantages: 

* sync ntuples will be produced for all samples by the participating groups, allowing for detailed synchronisation in datasets other than the usual signal samples (e.g. data, W+jets to check stitching, ttbar to check top pt reweighting, etc). 
* after synchronization, sync ntuples produced by the different groups can be made public to the team, allowing to reach a full set of ntuples for all datasets faster, and making it possible for new groups to participate in the final stage of the analysis right away. 

As a consequence, the sync ntuple is now called the **analysis ntuple.** 

## Event selection for the production of ntuples

As described in the [baseline selection](baseline_selection.md), no anti electron/muon discriminators, extra lepton vetoes, trigger(s) or filter(s) are applied when producing the sync ntuples. They are however stored as flags for later use. 

For taus the VVLooseIsolationMVArun2017v2 is applied. This is due to the fact that in NANOAOD only events that pass a OR of the loosest isolation WPs are stored (see [here](https://cms-nanoaod-integration.web.cern.ch/integration/master/mc94X_doc.html) under `nTau`). For electrons and muons no isolation is applied. 

**TODO THIS VERY LOOSE ISOLATION DOES NOT LOOK THE SAME AS THE ONE APPLIED E.G. IN THE [mu-tau channel](baseline_selection_mutau.md). IF IT'S THE SAME, BE MORE SPECIFIC HERE AND GIVE THE WORKING POINT.**

With the newly introduced data format it is now up to the analyst to use the usual MINIAOD or switch to the new NANOAOD samples. The synchronisation exercise needs to give the same results independently of this choice.

**Note:**

* When analysis-specific ntuples are produced, e.g. for analyses using a baseline selection that differs from the cuts detailed in the aforementioned section), this should be made clear in the .txt file uploaded to the sync repository. 
* It is up to the analysts to decide exactly which branches are included - not all are necessary or useful for all channels. 
* Please make sure to include only branches that can be obtained from both MINIAOD and NANOAOD. 

## Ntuple format

[analysis ntuple format](analysis_ntuple_format.md)

## List of synchronization ntuples

### Ntuple publication

Synchronisation ntuples will be collected in [https://github.com/CMS-HTT/2017-sync](https://github.com/CMS-HTT/2017-sync). To be able to push your ntuples there, you must become a member of the https://github.com/CMS-HTT organisation. To request access, just send an email to [Riccardo](mailto:riccardo.manzoni@cern.ch) or [Jan](mailto:jan.steggemann@cern.ch) with your github username.

### Signal datasets

Since the signal datasets are small, produce the synchronization ntuple for the full dataset.

* VBFHToTauTau_M125: 

```
/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM 
/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM
```

### Background datasets

Since background datasets are large, for the synchronization on background datasets, we can agree to process only the first 10k events of a specific input MINIAOD or NANOAOD file. 

To be discussed.


### Data 

Since data datasets are large, for the synchronization on data, we can agree to process only the first 10k events of a specific input MINIAOD or NANOAOD file. 

To be discussed.


## List of public analysis ntuples

None yet