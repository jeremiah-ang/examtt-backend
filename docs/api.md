# API

## API Root

```
/api/examtt
```

## Common terms
- **STUDENT NAME**: any String
- **MODULE CODE**: alphanumeric `i.e. CS4234, CS1101R`
- **EXAM DATE**: DDMMM. `i.e. 04DEC, 27NOV`
- **EXAM TIME**: 24-Hours HHMM. `i.e. 1330, 0130`
- **EXAM VENUE**: Matches A-Za-z0-9-_. `i.e. MPSH1A, COM1-0209`

## Adding a new timetable entry
API Endpoint: `/add/`
Request Body
```
{
    "examtt": {
        "name": <STUDENT NAME>,
        "modules": [
            {
                "module_code": <MODULE CODE>,
                "venue": <EXAM VENUE>,
                "date": <EXAM DATE>,
                "time": <EXAM TIME>
            }...
        ]
    }
}
```