import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *

def customise_particletop(process):
    if not hasattr(process, 'particleLevel'):
        process.load("PhysicsTools.NanoAOD.particlelevel_cff")

    process.genParticles2HepMC.signalParticlePdgIds = [6, -6]
    process.rivetLeptonTable.name = "RivetLepton" ## We change the name, default was GenDressedLepton
    
    process.rivetJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
        src = cms.InputTag("particleLevel:jets"),
        cut = cms.string(""),
        name= cms.string("RivetJet"),
        doc = cms.string("AK4 jets from Rivet-based ParticleLevelProducer"),
        singleton = cms.bool(False), # the number of entries is variable
        extension = cms.bool(False),
        variables = cms.PSet(
            # Identical to GenJets, so we just extend their flavor information
            P4Vars,
            hadronFlavour = Var("pdgId", int, doc="PDG id"),
        )
    )

    process.particleLevelTables += process.rivetJetTable

    return process
