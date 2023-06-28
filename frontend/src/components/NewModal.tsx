import { useForm } from 'react-hook-form';
import { useEffect, useState } from 'react';
import { Dialog, DialogTitle, DialogContent, DialogActions, TextField, Stack, Button, FormControl, Select, MenuItem, InputLabel } from '@mui/material';
interface MyFormProps {
    is_open: boolean;
    topic: string;
    formType: 'create' | 'update';
    schemaEndpoint: string;
    submitPoint: string;
    rawData?: any;
    onClose: () => void;
}
export const MyForm = ({ is_open, topic, formType, schemaEndpoint, rawData, submitPoint, onClose }: MyFormProps) => {
    const { register, handleSubmit, setValue } = useForm<any>({ defaultValues: rawData }); // Pass rawData as defaultValues to useForm hook
    const [schema, setSchema] = useState<any>(null);
    const [values, setValues] = useState<any>(rawData || {});
    const [visible, setVisible] = useState(is_open);

    const onSubmit = () => {
        console.log(submitPoint);
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(values), // send the form data
        };

        console.log(options.body);

        fetch(submitPoint, options)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // handle response
            })
            .catch(error => {
                console.error(error);
                // handle error
            });

        onClose();
    }
    useEffect(() => {
        // Fetch the schema data from the backend API
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'accept': 'application/json'
            },
            body: JSON.stringify({ /* data to be sent in the request body */ })
        };
        fetch(schemaEndpoint, options)
            .then(response => {
                console.log(response.body);
                return response.json();
            })
            .then(data => {
                console.log(data["info"]);
                setSchema(data["info"]);
                // perform additional actions here
            });
    }, [schemaEndpoint]);
    useEffect(() => {
        // Set default values for form fields from rawData when the component mounts
        Object.keys(rawData || {}).forEach((property) => {
            setValue(property, rawData?.[property]);
        });
    }, [rawData, setValue]);
    useEffect(() => {
        setVisible(is_open);
    }, [is_open]);
    return (
        schema ? (
            <Dialog open={visible}>
                <DialogTitle textAlign="center">
                    {formType === 'create' ? `Create ${topic}` : `Update ${topic}`}
                </DialogTitle>
                <DialogContent>
                    <form onSubmit={(e) => e.preventDefault()}>
                        <Stack
                            sx={{
                                width: '100%',
                                minWidth: { xs: '300px', sm: '360px', md: '400px' },
                                gap: '1.5rem',
                            }}
                        >
                            {Object.keys(schema || {}).map((property) => (
                                schema[property].type === 'enum' ?
                                    <FormControl key={property}>
                                        <InputLabel>{property}</InputLabel>
                                        <Select
                                            variant='standard'
                                            label={property}
                                            name={property}
                                            value={values[property]}
                                            onChange={(e) =>
                                                setValues({
                                                    ...values,
                                                    [e.target.name]: e.target.value,
                                                })
                                            }
                                        >
                                            {schema[property].enum.map((value: string) =>
                                                <MenuItem key={value} value={value}>{value}</MenuItem>
                                            )}
                                        </Select>
                                    </FormControl>
                                    :
                                    <TextField
                                        variant='standard'
                                        key={property}
                                        label={property}
                                        name={property}
                                        onChange={(e) => setValues({ ...values, [e.target.name]: e.target.value })}
                                    />
                            ))}
                        </Stack>
                    </form>
                </DialogContent>
                <DialogActions sx={{ p: '1.25rem' }}>
                    <Button onClick={onClose}>Cancel</Button>
                    <Button color="secondary" onClick={onSubmit} variant="contained">
                        {formType === 'create' ? `Create ${topic}` : `Update ${topic}`}
                    </Button>
                </DialogActions>
            </Dialog>
        ) : (
            <div>Loading schema...</div>
        )
    );
};