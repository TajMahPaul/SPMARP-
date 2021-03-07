import sqlite3

def main():
    conn = sqlite3.connect('surrey.db')
    c = conn.cursor()
    
    try:
        # Create tables
        c.execute('''CREATE TABLE IF NOT EXISTS waiting_points (name text PRIMARY KEY, FEDcode integer, FEDname text, lon real, lat real)''')
        c.execute('''CREATE TABLE IF NOT EXISTS demand_points (DAuid integer PRIMARY KEY, FEDcode integer, FEDname text, lon real, lat real, crime_index real, population_val real)''')
        c.execute('''CREATE TABLE IF NOT EXISTS crime_points (file_number text PRIMARY KEY, location_string text, month integer, year integer, lon real, lat real, closest_demand integers, distance real)''')
        c.execute('''CREATE TABLE IF NOT EXISTS distances (WPname name, DAuid integer, distance real)''')
    except Exception as e:
        raise(e)
    finally:
        # close connection and cursor
        c.close()
        conn.close()

if __name__ == "__main__":
    main()