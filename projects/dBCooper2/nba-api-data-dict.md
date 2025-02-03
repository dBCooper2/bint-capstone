# NBA_API :: Data Dictionary

## NBA Player Stats (2004-2024, `nba_player_stats_2004_2024`)

| Column Name          | Data Type | Description |
|----------------------|-----------|-------------|
| `Unnamed: 0`        | int64     | Index column, may be unnecessary |
| `player_id`         | int64     | Unique identifier for the player |
| `player_name`       | object    | Player's full name |
| `nickname`          | object    | Player's nickname (if available) |
| `team_id`           | int64     | Identifier for the team the player played for |
| `team_abbreviation` | object    | Short code for the team (e.g., LAL for Lakers) |
| `age`               | float64   | Age of the player in the given season |
| `gp`               | int64     | Games played |
| `w`                | int64     | Wins |
| `l`                | int64     | Losses |
| `w_pct`            | float64   | Win percentage |
| `min`              | float64   | Total minutes played |
| `fgm`              | int64     | Field goals made |
| `fga`              | int64     | Field goals attempted |
| `fg_pct`           | float64   | Field goal percentage |
| `fg3m`             | int64     | Three-point field goals made |
| `fg3a`             | int64     | Three-point field goals attempted |
| `fg3_pct`          | float64   | Three-point field goal percentage |
| `ftm`              | int64     | Free throws made |
| `fta`              | int64     | Free throws attempted |
| `ft_pct`           | float64   | Free throw percentage |
| `oreb`             | int64     | Offensive rebounds |
| `dreb`             | int64     | Defensive rebounds |
| `reb`              | int64     | Total rebounds |
| `ast`              | int64     | Assists |
| `tov`              | int64     | Turnovers |
| `stl`              | int64     | Steals |
| `blk`              | int64     | Blocks |
| `blka`             | int64     | Blocked attempts |
| `pf`               | int64     | Personal fouls |
| `pfd`              | int64     | Personal fouls drawn |
| `pts`              | int64     | Total points scored |
| `plus_minus`       | int64     | Plus/minus rating |
| `nba_fantasy_pts`  | float64   | Fantasy points for NBA fantasy leagues |
| `dd2`              | int64     | Double-doubles recorded |
| `td3`              | int64     | Triple-doubles recorded |
| `wnba_fantasy_pts` | float64   | Fantasy points for WNBA fantasy leagues |
| `gp_rank` to `wnba_fantasy_pts_rank` | int64 | Rank of the player in each category |
| `season`           | object    | Season in which stats were recorded (e.g., "2023-24") |

---

## NBA Team Stats (2004-2024, `nba_team_stats_2004_2024`)

| Column Name          | Data Type | Description |
|----------------------|-----------|-------------|
| `Unnamed: 0`        | int64     | Index column, may be unnecessary |
| `team_id`           | int64     | Unique identifier for the team |
| `team_name`         | object    | Name of the team |
| `gp`               | int64     | Games played |
| `w`                | int64     | Wins |
| `l`                | int64     | Losses |
| `w_pct`            | float64   | Win percentage |
| `min`              | float64   | Total minutes played |
| `fgm`              | int64     | Field goals made |
| `fga`              | int64     | Field goals attempted |
| `fg_pct`           | float64   | Field goal percentage |
| `fg3m`             | int64     | Three-point field goals made |
| `fg3a`             | int64     | Three-point field goals attempted |
| `fg3_pct`          | float64   | Three-point field goal percentage |
| `ftm`              | int64     | Free throws made |
| `fta`              | int64     | Free throws attempted |
| `ft_pct`           | float64   | Free throw percentage |
| `oreb`             | int64     | Offensive rebounds |
| `dreb`             | int64     | Defensive rebounds |
| `reb`              | int64     | Total rebounds |
| `ast`              | int64     | Assists |
| `tov`              | float64   | Turnovers |
| `stl`              | int64     | Steals |
| `blk`              | int64     | Blocks |
| `blka`             | int64     | Blocked attempts |
| `pf`               | int64     | Personal fouls |
| `pfd`              | int64     | Personal fouls drawn |
| `pts`              | int64     | Total points scored |
| `plus_minus`       | float64   | Plus/minus rating |
| `gp_rank` to `plus_minus_rank` | int64 | Rank of the team in each category |
| `season`           | object    | Season in which stats were recorded (e.g., "2023-24") |

