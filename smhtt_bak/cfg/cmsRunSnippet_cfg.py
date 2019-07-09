import FWCore.ParameterSet.Config as cms

### Global settings
data = True #needed in some recipes. For MC, set accordingly to `False`
process = cms.Process("UPDATE")
process.p = cms.Path()

### Configure update on Jets
# Performed updates:
# - rerun the JEC with the latest Global Tag. Details: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrPatJets
# - add DeepFlavour discriminators for b-tagging. Details: https://twiki.cern.ch/twiki/bin/view/CMS/DeepJet#94X_installation_recipe_X_10
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
updateJetCollection(
       process,
       jetSource = cms.InputTag('slimmedJets'),
       labelName = 'UpdatedJEC',
       jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),
       btagDiscriminators = [
            "pfDeepFlavourJetTags:probb",
            "pfDeepFlavourJetTags:probbb",
            "pfDeepFlavourJetTags:problepb",
       ],
)
process.jecSequence = cms.Sequence(process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC)
process.p *= process.jecSequence
jetCollection = cms.InputTag("updatedPatJetsUpdatedJEC") # to be used as input

### Configure update on Electrons
# Performed updates:
# - apply scale & smear corrections and store them as user floats. Details: https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPostRecoRecipes#2016_2017_Data_MC
# - recompute ID's including Fall17 V2 cut-based and MVA-based ID's. Details: https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentificationRun2#Recommended_MVA_Recipe_V2_for_re and https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Recipe_for_regular_users_formats
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(
        process,
        runVID=True,
        eleIDModules=[
                'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV70_cff',

                'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V1_cff',
                'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V1_cff',
                'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V1_cff',

                'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff',
                'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V2_cff',
                'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V2_cff',
        ],
        era='2017-Nov17ReReco'
)
process.p *= process.egammaPostRecoSeq
electronCollection = cms.InputTag("slimmedElectrons") # to be used as input
## Values to be accessed. Details: https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2#ID_information
# id decisions accessed via pat::Electron::electronID()
ids = cms.VInputTag(
    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto"),
    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose"),
    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium"),
    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight"),

    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-veto"),
    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-loose"),
    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-medium"),
    cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-tight"),

    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp90"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp80"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wpLoose"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wp90"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wp80"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wpLoose"),

    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp90"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp80"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wpLoose"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V2-wp90"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V2-wp80"),
    cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V2-wpLoose"),
)
# float MVA discriminator values accessed via pat::Electron::userFloat()
values = cms.vstring(
    "ElectronMVAEstimatorRun2Fall17NoIsoV1Values",
    "ElectronMVAEstimatorRun2Fall17IsoV1Values",
    "ElectronMVAEstimatorRun2Fall17NoIsoV2Values",
    "ElectronMVAEstimatorRun2Fall17IsoV2Values",
)
# scale & smear energy info (before & after correction) accessed via pat::Electron::userFloat()
energies = cms.vstring(
    "ecalTrkEnergyPreCorr",
    "ecalTrkEnergyPostCorr",
    "ecalTrkEnergyErrPreCorr",
    "ecalTrkEnergyErrPostCorr",
)
# systematic variations for scale & smear corrections (to be used on MC) accessed via pat::Electron::userFloat()
systematics = cms.vstring(
    "energyScaleUp",
    "energyScaleDown",
    "energyScaleStatUp",
    "energyScaleStatDown",
    "energyScaleSystUp",
    "energyScaleSystDown",
    "energyScaleGainUp",
    "energyScaleGainDown",
    "energySigmaUp",
    "energySigmaDown",
    "energySigmaPhiUp",
    "energySigmaPhiDown",
    "energySigmaRhoUp",
    "energySigmaRhoDown",
)

### Configure update on Taus
# Performed updates:
# - Compute Tau IDs against jets. Details: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#Rerunning_of_the_tau_ID_on_M_AN1 and https://indico.cern.ch/event/763206/contributions/3168445/attachments/1730010/2795612/mbluj_deepTauId_validation_28Sep2018.pdf
# - TODO incorporate also computation for new Anti-Electron MVA training. Details: https://indico.cern.ch/event/763206/contributions/3168444/attachments/1729998/2795591/mbluj_newAntiE_validation_3Oct2018.pdf
from RecoTauTag.RecoTau.runTauIdMVA import TauIDEmbedder
na = TauIDEmbedder(process, cms,
    debug=True,
    toKeep = ["2017v2","DPFTau_2016_v0","DPFTau_2016_v1","deepTau2017v1"]
)
taus = "NewTauIDsEmbedded"
na.runTauID(taus)
process.p *= ( process.rerunMvaIsolationSequence)
process.p *= getattr(process, taus)
tauCollection = cms.InputTag(taus) # to be used as input
# Tau ID's embedded additionally into the new collection
additionalIds = cms.vstring(
    "byIsolationMVArun2017v2DBoldDMwLTraw2017",
    "byVVLooseIsolationMVArun2017v2DBoldDMwLT2017",
    "byVLooseIsolationMVArun2017v2DBoldDMwLT2017",
    "byLooseIsolationMVArun2017v2DBoldDMwLT2017",
    "byMediumIsolationMVArun2017v2DBoldDMwLT2017",
    "byTightIsolationMVArun2017v2DBoldDMwLT2017",
    "byVTightIsolationMVArun2017v2DBoldDMwLT2017",
    "byVVTightIsolationMVArun2017v2DBoldDMwLT2017",
    "deepTau2017v1tauVSall",
    "DPFTau_2016_v0tauVSall",
    "DPFTau_2016_v1tauVSall",
)

### Configure update on MET
# Performed updates:
# - recorrect PF MET with Type-1 correction & EE noise mitigation (met recipe v2). Details: https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_9_for_2
# - FIXME Type-1 recorrection of PUPPI MET cannot be run together with PF MET correction because of overlapping module configurations. In contact with JetMET POG. Details: https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#Puppi_MET
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
runMetCorAndUncFromMiniAOD(
	process,
	isData=data,
	fixEE2017 = True,
	fixEE2017Params = {'userawPt': True, 'ptThreshold':50.0, 'minEtaThreshold':2.65, 'maxEtaThreshold': 3.139},
	postfix = "ModifiedMET"
)
process.p *= process.fullPatMetSequenceModifiedMET
pfMetCollection = cms.InputTag("slimmedMETsModifiedMET")
#from PhysicsTools.PatAlgos.slimming.puppiForMET_cff import makePuppiesFromMiniAOD
#makePuppiesFromMiniAOD(process, True)
#runMetCorAndUncFromMiniAOD(
#        process,
#        isData=data,
#        metType="Puppi",
#        postfix="Puppi",
#        jetFlavor="AK4PFPuppi",
#)
#
#process.puppiNoLep.useExistingWeights = False
#process.puppi.useExistingWeights = False
#
#process.p *= process.fullPatMetSequencePuppi
puppiMetCollection = cms.InputTag("slimmedMETsPuppi")

