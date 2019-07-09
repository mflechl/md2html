#!/bin/bash

### Basic CMSSW setup ###

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

scramv1 project CMSSW_9_4_11_cand2
cd CMSSW_9_4_11_cand2/src
eval `scramv1 runtime -sh`

git cms-init

### Add-packages ###

# Get DeepFlavour b-tagger (optional)
git cms-addpkg RecoBTag/TensorFlow
git cherry-pick 94ceae257f846998c357fcad408986cc8a039152

# Get working version of HTXSRivetProducer (mainly relevant for SM HTT)
#TODO the new version in CMSSW_9_4_11_cand1 is validated. To be followed up
git cms-addpkg GeneratorInterface/RivetInterface
cd GeneratorInterface/RivetInterface/plugins
rm HTXSRivetProducer.cc
wget https://raw.githubusercontent.com/perrozzi/cmssw/HTXS_clean/GeneratorInterface/RivetInterface/plugins/HTXSRivetProducer.cc
cd -

### Merge-topics ###

# Get code for electron V2 ID's (trained on 94X MC's)
git cms-merge-topic guitargeek:EgammaID_949

# Get code for electron scale & smear corrections
git cms-merge-topic cms-egamma:EgammaPostRecoTools_940

# Get recipes to re-correct MET (also for ECAL noise)
git cms-merge-topic cms-met:METFixEE2017_949_v2

# Get deep Tau & DPF based Tau ID (and Tau ID Embedder) (deep Tau & DPF Tau optional)
git cms-merge-topic ocolegro:dpfisolation # consists updated version of runTauIdMVA.py (RecoTauTag/RecoTau/python/runTauIdMVA.py). Originally, this .py file comes from https://raw.githubusercontent.com/greyxray/TauAnalysisTools/CMSSW_9_4_X_tau-pog_RunIIFall17/TauAnalysisTools/python/runTauIdMVA.py

# Get latest anti-e discriminator MVA6v2 (2017 training) (optional)
#TODO some files need to be copied from afs. A proper integration of the files will be done by Tau POG. To be followed up.
git cms-merge-topic cms-tau-pog:CMSSW_9_4_X_tau-pog_updateAntiEDisc

### Analysis group related software (ntuplizer, skimming, private MiniAOD, etc.) ###

#FIXME Add here your packages

scram b -j 8
