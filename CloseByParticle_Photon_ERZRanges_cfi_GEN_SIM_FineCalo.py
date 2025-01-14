# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: CloseByParticle_Photon_ERZRanges_cfi --conditions auto:phase2_realistic_T15 -n 100 --era Phase2C9 --eventcontent FEVTDEBUG --relval 9000,100 -s GEN,SIM --datatier GEN-SIM --beamspot HLLHC --geometry Extended2026D49 --no_exec --fileout file:step1.root --procModifier fineCalo
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')
options.register('generatorRandomSeed',
                 123456,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.int,
                 "Random seed for generator process")

options.register('pdgid',
                 22,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.int,
                 "PDG ID for particle gun")

options.register('minpT',
                 4.95,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "Minimum pT of CloseByPhotons")


options.register('maxpT',
                 5.05,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "Maximum pT of CloseByPhotons")



options.register('minEta',
                 1.69,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "Minimum eta of CloseByPhotons")

options.register('maxEta',
                 1.71,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "Maximum eta of CloseByPhotons")

options.register('minPhi',
                 -3.14159265359,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "Minimum phi of CloseByPhotons")

options.register('maxPhi',
                 3.14159265359,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "Maximum phi of CloseByPhotons")

options.register('minz',
                 320,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "Minimum z of CloseByPhotons")



options.maxEvents=1
options.parseArguments()



from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
from Configuration.ProcessModifiers.fineCalo_cff import fineCalo

process = cms.Process('SIM',Phase2C9,fineCalo)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedHLLHC_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(options.maxEvents),
        output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('CloseByParticle_Photon_ERZRanges_cfi nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')



process.generator = cms.EDProducer(
        "CloseByParticleGunProducer",
        AddAntiParticle = cms.bool(False),
        PGunParameters = cms.PSet(
                Delta = cms.double(20),
                PtMax = cms.double(options.maxpT),
                PtMin = cms.double(options.minpT),
                MaxEta = cms.double(options.maxEta),
                MinEta = cms.double(options.minEta),
                MaxPhi = cms.double(3.14159265359),
                MinPhi = cms.double(-3.14159265359),
                NParticles = cms.int32(1),
                Overlapping = cms.bool(False),
                PartID = cms.vint32(options.pdgid),
                Pointing = cms.bool(True),
                #RMax = cms.double(120),
                #RMin = cms.double(60),
                RandomShoot = cms.bool(False),
                ZMax = cms.double(options.minz+1),
                ZMin = cms.double(options.minz)
        ),
        Verbosity = cms.untracked.int32(0),
        firstRun = cms.untracked.uint32(1),
        psethack = cms.string('random particles in phi and eta windows')
)

process.RandomNumberGeneratorService.generator.initialSeed = options.generatorRandomSeed

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
