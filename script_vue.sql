CREATE VIEW IF NOT EXISTS vue_rendez_vous_by_user
    AS SELECT vrz.id, vrz.date_de_prise, vrz.date_consulation, vrz.raison, vrz.temps, vrz.prix, vrz.etat, c.id, c.nom, c.prenom FROM vet_rendez_vous vrz
        JOIN Client c 
            ON vrz.patient = c.id

INSERT INTO vet_client (nom, prenom, adresse, mail, contact)
VALUES
    ('Dupont', 'Jean', '123 Rue de la Paix, Paris', 'jean.dupont@example.com', '0123456789'),
    ('Martin', 'Marie', '456 Avenue des Fleurs, Lyon', 'marie.martin@example.com', '9876543210');

INSERT INTO vet_rendez_vous (date_de_prise, date_consultation, raison, temps, prix, patient, etat)
VALUES
    ('2023-06-01', '2023-06-10', 'Vaccination', 30, 50.00, 1, 1),
    ('2023-06-02', '2023-06-12', 'Consultation générale', 60, 80.00, 2, 1);
