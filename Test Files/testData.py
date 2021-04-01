driveInfo =[
    {
        "DriveName":"d1",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d2",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d3",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d4",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d5",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d6",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d7",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d8",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
    {
        "DriveName":"d9",
        "BreifDesc":"xbox",
        "DriveSize":"5",
        "DriveSizeMetric":"tb",
        "UseableSpaceOnDrive":"5",
        "RemainingSpaceOnDrive":"5",
        "NumberOfGamesOnDrive":"0"
    },
]
commands = [
    {
        "Username":"Tdeves1",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"userVerificationEngine.create_drive_entry(*jsonData['args'])",
        "for":"User",
        "args":["Tdeves1.db", driveDatabaseTBLayout, driveInfo[0]]
    },
    {
        "Username":"Bold",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Bold.db", driveDatabaseTBLayout, driveInfo[1]]
    },
    {
        "Username":"Frozen07",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Frozen07.db", driveDatabaseTBLayout, driveInfo[2]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[3]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[4]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[5]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[6]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[7]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[8]]
    }
]
